#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""爬取公司自建知识库网站（同域名限制）。仅用标准库。

用法：
  # 最简单的：给个入口，自动爬同域名下所有内链
  python tools/crawl_site.py "http://kb.company.com/" --cookie "SESSION=xxxx"

  # 需要登录的站点，从浏览器 F12 → Network → 任一请求 → 复制 Cookie 整行
  python tools/crawl_site.py "http://kb.company.com/" --cookie "..." --max-pages 500

  # 只爬某个路径前缀
  python tools/crawl_site.py "http://kb.company.com/faq/" --include "/faq/"

参数：
  --cookie      登录态 Cookie 字符串
  --max-pages   最多爬多少页（默认 200）
  --include     只保留 URL 含该子串的页面（可多次）
  --exclude     排除 URL 含该子串的页面（可多次）
  --category    强制分类（不填按关键词自动归类）
  --delay       每页间隔秒数（默认 0.8，别给公司服务器压力）
"""
import sys
import time
import re
import argparse
import urllib.request
import urllib.parse
import urllib.error
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import write_doc, guess_category, html_to_text, strip_markdown

SKIP_EXT = {".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".css", ".js",
            ".zip", ".rar", ".7z", ".exe", ".mp4", ".mp3", ".pdf", ".doc",
            ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".ico", ".woff", ".woff2", ".ttf"}


def fetch(url, cookie, timeout=20):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) KB-Importer/1.0",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
        ctype = r.headers.get("Content-Type", "")
        if "html" not in ctype and "text" not in ctype:
            return None, ctype
        for enc in ("utf-8", "gbk", "gb18030"):
            try:
                return raw.decode(enc), ctype
            except UnicodeDecodeError:
                continue
        return raw.decode("utf-8", "ignore"), ctype


def extract_main(html):
    """尽量只取正文区域，去掉导航/页脚。"""
    for pat in (r"(?is)<article[^>]*>(.*?)</article>",
                r"(?is)<main[^>]*>(.*?)</main>",
                r"(?is)<div[^>]+(?:class|id)=\"[^\"]*(?:content|article|main|markdown|detail|doc-body)[^\"]*\"[^>]*>(.*?)</div>\s*(?:</div>|<footer)"):
        m = re.search(pat, html)
        if m and len(m.group(1)) > 400:
            return m.group(1)
    return html


def get_title(html):
    m = re.search(r"(?is)<title>(.*?)</title>", html)
    if m:
        t = html_to_text(m.group(1))
        t = re.sub(r"\s*[-_|｜]\s*[^-_|｜]{0,20}$", "", t).strip()
        if t:
            return t
    m = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", html)
    return html_to_text(m.group(1)) if m else ""


def links(html, base, host):
    out = []
    for m in re.finditer(r"(?is)<a[^>]+href=[\"']([^\"'#]+)[\"']", html):
        href = m.group(1).strip()
        if href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        full = urllib.parse.urljoin(base, href)
        p = urllib.parse.urlparse(full)
        if p.scheme not in ("http", "https") or p.netloc != host:
            continue
        if Path(p.path).suffix.lower() in SKIP_EXT:
            continue
        clean = urllib.parse.urlunparse((p.scheme, p.netloc, p.path, "", p.query, ""))
        out.append(clean.split("#")[0])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start", help="入口 URL")
    ap.add_argument("--cookie", default="")
    ap.add_argument("--max-pages", type=int, default=200)
    ap.add_argument("--include", action="append", default=[])
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--category", default="")
    ap.add_argument("--delay", type=float, default=0.8)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    start = args.start
    host = urllib.parse.urlparse(start).netloc
    if not host:
        raise SystemExit("URL 需要带 http:// 或 https://")

    seen, queue, pages = set(), [start], []

    while queue and len(pages) < args.max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        if any(x in url for x in args.exclude):
            continue
        if args.include and not any(x in url for x in args.include):
            continue
        try:
            html, ctype = fetch(url, args.cookie)
        except urllib.error.HTTPError as e:
            print(f"  ! {e.code} {url}")
            continue
        except Exception as e:
            print(f"  ! {url} -> {e}")
            continue
        if not html:
            continue
        title = get_title(html) or url.rstrip("/").split("/")[-1] or "未命名"
        body = html_to_text(extract_main(html))
        if len(body) < 60:
            # 正文太短，可能只是列表页，仍然继续抓链接
            pass
        else:
            pages.append({"url": url, "title": title, "body": body})
        print(f"  [{len(pages)}] {title[:40]}  ({len(body)}字)")
        for l in links(html, url, host):
            if l not in seen and len(queue) < args.max_pages * 3:
                queue.append(l)
        time.sleep(args.delay)

    if not pages:
        print("没抓到任何页面。检查入口 URL、Cookie 或 --include 过滤条件。")
        return 1

    # 去掉站点模板（在多数页面都出现的短行：导航、页脚）
    print(f"\n共抓到 {len(pages)} 个页面，开始去模板噪声…")
    line_counter = Counter()
    for p in pages:
        uniq = {ln for ln in p["body"].splitlines() if 0 < len(ln) <= 40}
        line_counter.update(uniq)
    n = len(pages)
    noise = {ln for ln, c in line_counter.items() if c >= max(3, n * 0.6)}

    ok = 0
    for p in pages:
        body = "\n".join(ln for ln in p["body"].splitlines()
                         if ln.strip() and ln.strip() not in noise)
        if len(body) < 60:
            continue
        cat = args.category or guess_category(p["title"], strip_markdown(body))[0]
        if args.dry_run:
            print(f"  [预览] {p['title']} → {cat}")
            ok += 1
            continue
        write_doc(title=p["title"], body=body, category=cat, source="官网",
                  url=p["url"], tags=[urllib.parse.urlparse(p["url"]).path.strip("/").split("/")[0]])
        ok += 1

    print(f"完成：{ok} 篇写入 docs/。下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
