#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""抓取公司 KMS 知识库（泛微系，服务端渲染）。仅用标准库。

用法：
  python tools/scrape_kms.py https://kms.gzych.vip
  python tools/scrape_kms.py https://kms.gzych.vip --limit 5      # 试跑
  python tools/scrape_kms.py https://kms.gzych.vip --max-pages 80

原理：
  列表页 webtype/view/Pub{n}.html 每页 10 篇，翻页直到没有新文档；
  正文页 webdoc/view/Pub<id>.html，正文在 <div class="ke-content"> 里。
"""
import re
import sys
import time
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import DOCS_DIR, write_doc, guess_category, strip_markdown

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

ENT = {"&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"',
       "&#39;": "'", "&ldquo;": "“", "&rdquo;": "”", "&mdash;": "—",
       "&hellip;": "…", "&times;": "×", "&middot;": "·"}


def get(url, timeout=30, retries=2):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA, "Accept-Language": "zh-CN,zh;q=0.9"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
            for enc in ("utf-8", "gbk", "gb18030"):
                try:
                    return raw.decode(enc)
                except UnicodeDecodeError:
                    continue
            return raw.decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < retries:
                time.sleep(2)
                continue
            return None
        except Exception:
            if attempt < retries:
                time.sleep(1.5)
    return None


def text_of(frag):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", frag or "")
    s = re.sub(r"(?s)<[^>]+>", "", s)
    for k, v in ENT.items():
        s = s.replace(k, v)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    return re.sub(r"\s+", " ", s).strip()


def extract_block(html, marker="ke-content"):
    """取 class 含 marker 的 div 的完整内部 HTML（按 div 深度配对）。"""
    i = html.find(marker)
    if i < 0:
        return ""
    start = html.rfind("<div", 0, i)
    if start < 0:
        return ""
    depth = 0
    for m in re.finditer(r"<(/?)div\b", html[start:]):
        if not m.group(1):
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                return html[start:start + m.end() + 6]
    return html[start:]


def html_to_md(frag, base):
    if not frag:
        return ""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", frag)

    def _img(m):
        src = m.group(1).strip()
        if src.startswith("data:"):
            return ""
        if src.startswith("//"):
            src = "https:" + src
        else:
            src = urllib.parse.urljoin(base, src)
        return "\n\n![](" + src + ")\n\n"
    s = re.sub(r"(?is)<img[^>]+?src=[\"']([^\"']+)[\"'][^>]*>", _img, s)

    # 表格先整体转成 Markdown 管道表，否则单元格会被后面的段落换行拍平
    def _table(m):
        rows = re.findall(r"(?is)<tr[^>]*>(.*?)</tr>", m.group(0))
        lines = []
        for idx, r in enumerate(rows):
            cells = re.findall(r"(?is)<t[dh][^>]*>(.*?)</t[dh]>", r)
            cells = [re.sub(r"\s+", " ", text_of(c)).strip() for c in cells]
            if not any(cells):
                continue
            lines.append("| " + " | ".join(cells) + " |")
            if idx == 0:
                lines.append("|" + "|".join([" --- "] * len(cells)) + "|")
        return "\n\n" + "\n".join(lines) + "\n\n" if lines else ""
    s = re.sub(r"(?is)<table[^>]*>.*?</table>", _table, s)

    for i in range(1, 5):
        s = re.sub(r"(?is)<h%d[^>]*>(.*?)</h%d>" % (i, i),
                   lambda m, i=i: "\n" + "#" * i + " " + text_of(m.group(1)) + "\n", s)
    s = re.sub(r"(?is)<li[^>]*>", "\n- ", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    s = re.sub(r"(?is)</p>", "\n\n", s)
    s = re.sub(r"(?is)</tr>", "\n", s)
    s = re.sub(r"(?is)</t[dh]>", " | ", s)
    s = re.sub(r"(?is)<[^>]+>", "", s)
    for k, v in ENT.items():
        s = s.replace(k, v)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    s = re.sub(r"[ \t\u00a0]+", " ", s)
    s = re.sub(r" *\| *\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    s = "\n".join(ln.strip() for ln in s.splitlines())
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def existing_urls():
    done = set()
    for p in DOCS_DIR.rglob("*.md"):
        try:
            head = p.read_text(encoding="utf-8")[:900]
        except Exception:
            continue
        m = re.search(r"(?m)^url:\s*(\S+)\s*$", head)
        if m:
            done.add(m.group(1))
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("base", help="站点根地址，如 https://kms.gzych.vip")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-pages", type=int, default=80, help="列表最多翻多少页")
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    base = args.base.rstrip("/")
    print(f"扫描列表：{base}/webtype/view/Pub1.html")

    ids, order = [], []
    for page in range(1, args.max_pages + 1):
        url = f"{base}/webtype/view/Pub{page}.html"
        html = get(url)
        if not html:
            print(f"  第 {page} 页取不到，停止翻页")
            break
        found = re.findall(r"webdoc/view/Pub([0-9a-f]{20,})\.html", html)
        new = [x for x in dict.fromkeys(found) if x not in ids]
        if not new:
            print(f"  第 {page} 页无新文档，翻页结束")
            break
        for x in new:
            ids.append(x)
            order.append(x)
        print(f"  第 {page} 页 +{len(new)}，累计 {len(ids)}")
        time.sleep(args.delay)

    print(f"共发现 {len(ids)} 篇文档")
    done = set() if args.force else existing_urls()

    ok = skip = fail = 0
    for i, doc_id in enumerate(order, 1):
        if args.limit and ok >= args.limit:
            print(f"达到 --limit {args.limit}，停止")
            break
        url = f"{base}/webdoc/view/Pub{doc_id}.html"
        if url in done:
            skip += 1
            continue
        html = get(url)
        if not html:
            print(f"  ! 取不到 {url}")
            fail += 1
            continue

        title = ""
        m = re.search(r'(?is)<div class="doc_title"[^>]*>(.*?)</div>', html)
        if m:
            title = text_of(m.group(1))
        if not title:
            m = re.search(r"<title>(.*?)</title>", html)
            title = text_of(m.group(1)).replace("-油菜花知识库", "").strip()
        if not title:
            print(f"  ! 无标题 {url}")
            fail += 1
            continue

        crumb = re.findall(r'<a href="webtype/view[^"]+"[^>]*title="([^"]+)"', html)
        crumb = [c for c in dict.fromkeys(crumb) if c]
        section = crumb[1] if len(crumb) >= 2 else (crumb[0] if crumb else "")

        body_html = extract_block(html)
        md = html_to_md(body_html, url)
        if len(strip_markdown(md)) < 20:
            print(f"  ! 正文为空（可能需登录）：{title}")
            fail += 1
            continue

        author = ""
        m = re.search(r'class="authortagsearch" title="([^"]*)"', html)
        if m:
            author = m.group(1)

        updated = ""
        m = re.search(r"(\d{4})年(\d{2})月(\d{2})日", html)
        if m:
            updated = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"

        code = ""
        m = re.search(r'title="知识ID">\s*([0-9A-Za-z]+)\s*<', html)
        if m:
            code = m.group(1)

        cat, _ = guess_category(title, strip_markdown(md))
        write_doc(title=title, body=md, category=cat, tags=[],
                  source="KMS", url=url, updated=updated or None,
                  extra_meta={"section": section, "toc_path": " / ".join(crumb),
                              "author": author, "kms_id": code})
        ok += 1
        print(f"  [{ok}] {title[:40]}  →  {cat}")
        time.sleep(args.delay)

    print(f"\n完成：新增 {ok} 篇，跳过已存在 {skip} 篇，失败 {fail} 篇")
    print("下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
