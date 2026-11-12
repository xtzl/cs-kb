#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按当前 classify_rules.json 重新归类已有文档（会移动文件到对应子目录）。

用法：
  python tools/reclassify.py            # 全部重算
  python tools/reclassify.py --dry-run  # 只看结果，不动文件
  python tools/reclassify.py --source 语雀   # 只处理某个来源

改完规则后跑一次，比重新导入快得多。
"""
import re
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import DOCS_DIR, strip_markdown, slugify, guess_category


def split_fm(text):
    """按行切 front matter（标题里可能含 --- ，不能直接 split）。"""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, min(len(lines), 100)):
            if lines[i].strip() == "---":
                return "\n".join(lines[1:i]), "\n" + "\n".join(lines[i+1:])
    return "", text


def get_field(fm, key):
    m = re.search(r"(?m)^" + key + r":\s*(.*)$", fm)
    return m.group(1).strip() if m else ""


def set_field(fm, key, value):
    if re.search(r"(?m)^" + key + r":", fm):
        return re.sub(r"(?m)^" + key + r":.*$", f"{key}: {value}", fm, count=1)
    return fm.rstrip("\n") + f"\n{key}: {value}\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--source", default="", help="只处理该来源（包含匹配）")
    args = ap.parse_args()

    files = sorted(DOCS_DIR.rglob("*.md"))
    changed, moved = 0, 0
    dist = {}

    for path in files:
        text = path.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        src = get_field(fm, "source")
        if args.source and args.source not in src:
            continue
        title = get_field(fm, "title") or path.stem
        old_cat = get_field(fm, "category") or "其他"
        # 目录名（section / toc_path）本身带业务信息，一起作为归类依据
        section = get_field(fm, "section")
        toc_path = get_field(fm, "toc_path")
        hint = " ".join(x for x in (title, section, toc_path) if x)
        new_cat, _ = guess_category(hint, strip_markdown(body))
        dist[new_cat] = dist.get(new_cat, 0) + 1

        if new_cat == old_cat:
            continue
        changed += 1
        if args.dry_run:
            print(f"  {old_cat} → {new_cat} | {title}")
            continue

        new_fm = set_field(fm, "category", new_cat)
        target_dir = DOCS_DIR / slugify(new_cat)
        target_dir.mkdir(parents=True, exist_ok=True)
        new_path = target_dir / path.name
        if new_path.exists() and new_path.resolve() != path.resolve():
            new_path = target_dir / f"{path.stem}-{abs(hash(title)) % 9999}.md"
        path.write_text("---\n" + new_fm.strip("\n") + "\n---" + body, encoding="utf-8")
        if new_path.resolve() != path.resolve():
            path.rename(new_path)
            moved += 1

    print(f"\n重新归类 {changed} 篇（移动文件 {moved} 个）")
    print("新分布：")
    for c, n in sorted(dist.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")
    print("下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
