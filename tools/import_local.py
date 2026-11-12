#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导入本地导出文件。

支持 md / txt / html / docx（含语雀、飞书导出的 Markdown 压缩包解压后的目录）。

用法：
  python tools/import_local.py "C:/路径/语雀导出" --source 语雀
  python tools/import_local.py "C:/路径/知识库.md" --category 系统操作
  python tools/import_local.py "D:/客服文档" --category 收银与对账 --dry-run

参数：
  --source    来源标签，默认「本地」
  --category  强制分类（不填则用子文件夹名，再不行归「其他」）
  --dry-run   只看会导入什么，不写文件
  --overwrite 同名覆盖（默认追加编号，不会覆盖已有文档）
"""
import sys
import argparse
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import (DOCS_DIR, docx_to_text, html_to_text, write_doc,
                    slugify, VALID_EXT_TEXT)

SKIP_NAMES = {"readme.md", "index.md", "_sidebar.md", "summary.md"}


def read_any(path: Path):
    ext = path.suffix.lower()
    if ext == ".docx":
        return docx_to_text(path)
    if ext in (".html", ".htm"):
        raw = path.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"(?is)<title>(.*?)</title>", raw)
        title = html_to_text(m.group(1)) if m else ""
        return f"# {title}\n\n{html_to_text(raw)}" if title else html_to_text(raw)
    if ext in (".md", ".markdown", ".txt"):
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return path.read_text(encoding="gbk", errors="ignore")
    return ""


def guess_title(path: Path, body: str):
    m = re.search(r"(?m)^\s{0,3}#\s+(.+)$", body)
    if m:
        return m.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="文件或目录路径")
    ap.add_argument("--source", default="本地")
    ap.add_argument("--category", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    root = Path(args.input).expanduser()
    if not root.exists():
        print(f"路径不存在：{root}")
        return 1

    if root.is_file():
        files = [root]
    else:
        files = [p for p in root.rglob("*")
                 if p.is_file() and p.suffix.lower() in VALID_EXT_TEXT]
        files = [p for p in files if p.name.lower() not in SKIP_NAMES]

    print(f"发现 {len(files)} 个可导入文件")
    ok = skip = 0
    for f in files:
        body = read_any(f)
        if not body or len(body.strip()) < 20:
            skip += 1
            continue
        title = guess_title(f, body)
        # 去掉正文里重复的一级标题
        body = re.sub(r"(?m)^\s{0,3}#\s+" + re.escape(title) + r"\s*$", "", body, count=1).strip()

        category = args.category
        if not category and f.parent != root and root.is_dir():
            category = f.parent.name
        if not category:
            category = "其他"

        tags = []
        m = re.search(r"(?m)^\s*(?:tags?|标签)\s*[:：]\s*(.+)$", body)
        if m:
            tags = [t.strip() for t in re.split(r"[,，;；]", m.group(1)) if t.strip()][:8]
            body = body.replace(m.group(0), "")

        if args.dry_run:
            print(f"  [预览] {title}  →  {category}  ({len(body)}字)")
            ok += 1
            continue

        write_doc(title=title, body=body, category=category, tags=tags,
                  source=args.source, updated=None)
        ok += 1

    print(f"完成：导入 {ok} 篇，跳过 {skip} 个空/过短文件")
    if not args.dry_run:
        print("下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
