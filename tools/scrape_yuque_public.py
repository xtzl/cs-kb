#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取「公开可读」的语雀知识库（无需 token）。仅用标准库。

用法：
  python tools/scrape_yuque_public.py https://ychylb.yuque.com/staff-gcg8pk/ylgj
  python tools/scrape_yuque_public.py https://ychylb.yuque.com/staff-gcg8pk/ylgj --limit 10
  python tools/scrape_yuque_public.py https://ychylb.yuque.com/staff-gcg8pk/ylgj --delay 0.4

原理：
  1. 知识库首页 HTML 里嵌了 window.appData（URL 编码的 JSON），含 book.id 与完整目录树
  2. 每篇文档走 /api/docs/{slug}?book_id=xxx&mode=markdown，返回 sourcecode 即 Markdown 原文
  3. 已导入过的（front matter 里 url 相同的）自动跳过，可反复执行增量更新
"""
import re
import sys
import json
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import (DOCS_DIR, write_doc, guess_category, strip_markdown)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def get(url, referer=None, timeout=30, retries=2):
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "text/html,application/json,*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": referer or url,
        })
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries:
                time.sleep(2 * (attempt + 1))
                continue
            if e.code in (401, 403, 404):
                return None
            time.sleep(1)
        except Exception:
            if attempt < retries:
                time.sleep(1.5 * (attempt + 1))
    return None


def appdata(html):
    m = re.search(r'window\.appData\s*=\s*JSON\.parse\(decodeURIComponent\("([^"]+)"', html)
    if not m:
        return None
    try:
        return json.loads(urllib.parse.unquote(m.group(1)))
    except Exception:
        return None


def parse_target(raw):
    """从 URL 或 namespace 里解析出 host / namespace / book_slug"""
    raw = raw.strip().rstrip("/")
    if raw.startswith("http"):
        p = urllib.parse.urlparse(raw)
        parts = [x for x in p.path.split("/") if x]
        # /staff-gcg8pk/ylgj 或 /user/book
        if len(parts) >= 2:
            return p.scheme + "://" + p.netloc, parts[0] + "/" + parts[1], parts[1]
        if len(parts) == 1:
            return p.scheme + "://" + p.netloc, parts[0], parts[0]
        raise SystemExit("URL 里没有知识库路径")
    if "/" in raw:
        ns, slug = raw.rsplit("/", 1)
        return "https://www.yuque.com", raw, slug
    return "https://www.yuque.com", raw, raw


def existing_urls():
    done = set()
    for p in DOCS_DIR.rglob("*.md"):
        try:
            head = p.read_text(encoding="utf-8")[:600]
        except Exception:
            continue
        m = re.search(r"(?m)^url:\s*(\S+)\s*$", head)
        if m:
            done.add(m.group(1))
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="知识库 URL 或 namespace，例如 staff-gcg8pk/ylgj")
    ap.add_argument("--delay", type=float, default=0.35)
    ap.add_argument("--limit", type=int, default=0, help="最多抓多少篇，0=全部")
    ap.add_argument("--force", action="store_true", help="忽略增量检查，全部重抓")
    args = ap.parse_args()

    host, ns, slug = parse_target(args.target)
    book_url = f"{host}/{ns}"
    print(f"读取知识库首页：{book_url}")
    html = get(book_url)
    if not html:
        raise SystemExit("首页打不开。确认这个知识库是公开可读的。")
    d = appdata(html)
    if not d:
        raise SystemExit("首页里没找到 appData，语雀可能改了页面结构。")
    book = d.get("book") or {}
    toc = book.get("toc") or []
    if not toc:
        raise SystemExit("没有取到目录。")
    print(f"知识库：{book.get('name')}  (id={book.get('id')}, 文档 {book.get('items_count')} 篇, 目录条目 {len(toc)})")

    # 展开目录层级 -> 每篇文档的 path
    docs = []
    stack = []
    for t in toc:
        lv = t.get("level") or 0
        title = (t.get("title") or "").strip()
        stack = stack[:lv]
        if t.get("type") == "TITLE":
            stack.append(title)
        elif t.get("type") == "DOC" and t.get("url"):
            docs.append({
                "slug": t["url"],
                "title": title,
                "path": stack[:],
            })

    print(f"待抓取文档 {len(docs)} 篇")
    done = set() if args.force else existing_urls()
    ok = skip = fail = 0

    for i, doc in enumerate(docs, 1):
        if args.limit and ok >= args.limit:
            print(f"达到 --limit {args.limit}，停止。")
            break
        url = f"{host}/{ns}/{doc['slug']}"
        if url in done:
            skip += 1
            continue
        api = (f"{host}/api/docs/{doc['slug']}"
               f"?book_id={book.get('id')}&mode=markdown&merge_dynamic_data=false")
        raw = get(api, referer=url)
        if not raw:
            print(f"  ! [{i}/{len(docs)}] 取不到：{doc['title']}")
            fail += 1
            continue
        try:
            data = json.loads(raw).get("data") or {}
        except Exception:
            data = {}
        body = (data.get("sourcecode") or "").strip()
        if not body:
            print(f"  ! [{i}/{len(docs)}] 空内容：{doc['title']}")
            fail += 1
            continue

        title = (data.get("title") or doc["title"] or "未命名").strip()
        section = doc["path"][0] if doc["path"] else ""
        path_str = " / ".join(doc["path"]) if doc["path"] else ""
        cat, _ = guess_category(title, strip_markdown(body))

        tags = []
        for kw, tag in (("电玩城", "电玩城"), ("家庭娱乐中心", "家庭娱乐中心"),
                        ("娃娃机", "娃娃机"), ("票务", "票务"), ("潮玩", "潮玩运动馆"),
                        ("盈客宝", "盈客宝"), ("团购", "团购核销"), ("兑币机", "兑币机")):
            if kw in path_str or kw in title:
                tags.append(tag)

        write_doc(
            title=title,
            body=body,
            category=cat,
            tags=tags,
            source=f"语雀·{book.get('name') or '娱乐管家'}",
            url=url,
            updated=(data.get("content_updated_at") or "")[:10] or None,
            extra_meta={"section": section, "toc_path": path_str},
        )
        ok += 1
        print(f"  [{ok}] {title}  →  {cat}" + (f"  ({path_str})" if path_str else ""))
        time.sleep(args.delay)

    print(f"\n完成：新增 {ok} 篇，跳过已存在 {skip} 篇，失败 {fail} 篇")
    print("下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
