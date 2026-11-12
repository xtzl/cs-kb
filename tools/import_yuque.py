#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从语雀（yuque.com）拉取知识库文档。仅用标准库。

准备：语雀 → 头像 → 设置 → Token → 新建，复制 token。
用法：
  set YUQUE_TOKEN=你的token
  python tools/import_yuque.py --list                 # 先看看有哪些知识库
  python tools/import_yuque.py                        # 全量导入
  python tools/import_yuque.py --book 客服手册        # 只导一个知识库
  python tools/import_yuque.py --category 系统操作     # 强制归到某个分类
  python tools/import_yuque.py --group mygroup        # 导入团队/群组知识库

说明：不指定 --category 时，会按关键词自动归类；识别不出归「其他」。
"""
import os
import sys
import json
import time
import argparse
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import write_doc, guess_category, html_to_text, strip_markdown

BASE = "https://www.yuque.com/api/v2"


def api(path, token, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "X-Auth-Token": token,
        "User-Agent": "kb-importer/1.0",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:200]
        if e.code in (401, 403):
            raise SystemExit(f"认证失败({e.code})：token 无效或无权限。{body}")
        if e.code == 429:
            raise SystemExit("触发语雀频率限制，请稍后重试（或减少 --limit 文档数）。")
        print(f"  ! 请求失败 {path} -> {e.code} {body}")
        return None
    except Exception as e:
        print(f"  ! 网络错误 {path}: {e}")
        return None


def paginate(path, token, key="data", limit=100, max_items=1000):
    out, offset = [], 0
    while offset < max_items:
        d = api(path, token, {"offset": offset, "limit": limit})
        if not d:
            break
        items = d.get(key) or []
        out.extend(items)
        if len(items) < limit:
            break
        offset += limit
        time.sleep(0.4)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("YUQUE_TOKEN", ""))
    ap.add_argument("--list", action="store_true", help="只列出知识库")
    ap.add_argument("--book", default="", help="只导入名字包含该词的知识库")
    ap.add_argument("--group", default="", help="群组/团队 login")
    ap.add_argument("--category", default="", help="强制分类")
    ap.add_argument("--limit", type=int, default=300, help="最多导入多少篇")
    ap.add_argument("--sleep", type=float, default=0.6)
    args = ap.parse_args()

    if not args.token:
        raise SystemExit("缺少 token：set YUQUE_TOKEN=xxx 或加 --token xxx")

    me = api("/user", args.token)
    if not me or not me.get("data"):
        raise SystemExit("无法读取用户信息，token 可能无效。")
    login = me["data"]["login"]
    print(f"已登录语雀：{me['data'].get('name', login)} ({login})")

    if args.group:
        books = paginate(f"/groups/{args.group}/repos", args.token)
    else:
        books = paginate(f"/users/{login}/repos", args.token)

    books = [b for b in books if isinstance(b, dict)]
    if args.book:
        books = [b for b in books if args.book in (b.get("name") or "")]

    if not books:
        raise SystemExit("没有找到知识库。私有知识库需要 token 具备读取权限。")

    print(f"共 {len(books)} 个知识库：")
    for b in books:
        print(f"  - {b.get('name')}  [{b.get('namespace')}]  {b.get('items_count', '?')} 篇")
    if args.list:
        return 0

    total = 0
    for b in books:
        ns = b.get("namespace")
        if not ns:
            continue
        print(f"\n== 导入知识库：{b.get('name')} ({ns})")
        docs = paginate(f"/repos/{ns}/docs", args.token, max_items=args.limit)
        for i, d in enumerate(docs, 1):
            if total >= args.limit:
                print(f"达到 --limit {args.limit}，停止。")
                return 0
            slug = d.get("slug") or d.get("id")
            if not slug:
                continue
            detail = api(f"/repos/{ns}/docs/{slug}", args.token)
            if not detail or not detail.get("data"):
                continue
            data = detail["data"]
            title = (data.get("title") or d.get("title") or "未命名").strip()
            body = data.get("body") or ""
            if not body.strip():
                body = html_to_text(data.get("body_html") or data.get("body_draft") or "")
            if not body.strip():
                print(f"  - 跳过（空内容）：{title}")
                continue

            if args.category:
                cat = args.category
            else:
                cat, _ = guess_category(title, strip_markdown(body))

            write_doc(
                title=title, body=body, category=cat,
                tags=[b.get("name", "")],
                source="语雀",
                url=f"https://www.yuque.com/{ns}/{slug}",
                updated=(data.get("updated_at") or "")[:10] or None,
                extra_meta={"book": b.get("name", "")},
            )
            total += 1
            print(f"  [{total}] {title}  →  {cat}")
            time.sleep(args.sleep)

    print(f"\n完成：共导入 {total} 篇。下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
