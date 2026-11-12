#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 docs/ 下所有 markdown，生成 data/index.json 和 data/index.js。
用法：python tools/build_index.py
"""
import sys
import json
import re
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import (ROOT, DOCS_DIR, DATA_DIR, CONFIG_DIR,
                    load_json, categories, strip_markdown)


def parse_front_matter(text):
    """按行解析 front matter。不能用 split('---')，因为标题里可能自带 --- 。"""
    meta, body = {}, text
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for i in range(1, min(len(lines), 100)):
            if lines[i].strip() == "---":
                for line in lines[1:i]:
                    if ":" in line and not line.strip().startswith("#"):
                        k, v = line.split(":", 1)
                        meta[k.strip().lower()] = v.strip()
                body = "\n".join(lines[i+1:])
                return meta, body.lstrip("\n")
    return meta, body


def parse_tags(raw):
    if not raw:
        return []
    raw = raw.strip().strip("[]")
    parts = re.split(r"[,，;；|]", raw)
    return [p.strip().strip('"\'') for p in parts if p.strip()]


def first_heading(body):
    for line in body.splitlines():
        m = re.match(r"^\s{0,3}#{1,3}\s*(.+)$", line)
        if m:
            return m.group(1).strip()
    return ""


def main():
    if not DOCS_DIR.exists():
        print(f"找不到 {DOCS_DIR}")
        return 1

    cat_order = categories()
    docs = []
    seen_cats = {}
    errors = []

    for path in sorted(DOCS_DIR.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = path.read_text(encoding="gbk", errors="ignore")
        except Exception as e:
            errors.append(f"{path.name}: {e}")
            continue

        meta, body = parse_front_matter(text)
        title = meta.get("title") or first_heading(body) or path.stem
        category = (meta.get("category") or "").strip() or "未分类"
        tags = parse_tags(meta.get("tags") or meta.get("标签"))
        source = (meta.get("source") or "本地").strip()
        updated = (meta.get("updated") or "").strip()
        url = (meta.get("url") or "").strip()
        aliases = parse_tags(meta.get("aliases") or meta.get("别名"))
        section = (meta.get("section") or "").strip()
        toc_path = (meta.get("toc_path") or "").strip()

        plain = strip_markdown(body)
        if not plain.strip():
            # 纯截图、没有文字的文档：用标题兜底，绝不能回退到全文（会把 front matter 当正文）
            plain = title.strip()

        rel = path.relative_to(DOCS_DIR).as_posix()
        doc_id = rel[:-3] if rel.endswith(".md") else rel

        docs.append({
            "id": doc_id,
            "title": title.strip(),
            "category": category,
            "tags": tags,
            "aliases": aliases,
            "source": source,
            "updated": updated,
            "url": url,
            "path": f"docs/{rel}",
            "section": section,
            "toc_path": toc_path,
            "summary": plain[:160].replace("\n", " "),
            "content": plain,
            "md": body.strip(),
            "chars": len(plain),
        })
        seen_cats[category] = seen_cats.get(category, 0) + 1

    # 分类顺序：配置里的顺序优先，其余追加
    ordered = [c for c in cat_order if c in seen_cats]
    ordered += sorted([c for c in seen_cats if c not in cat_order])

    # 标签统计
    tag_count = {}
    for d in docs:
        for t in d["tags"]:
            tag_count[t] = tag_count.get(t, 0) + 1
    top_tags = sorted(tag_count.items(), key=lambda x: (-x[1], x[0]))[:40]

    syn = load_json(CONFIG_DIR / "synonyms.json", {}) or {}
    groups = [g for g in syn.get("groups", []) if isinstance(g, list) and g]
    syn_map = {}
    for g in groups:
        for w in g:
            syn_map.setdefault(w, set()).update(g)
    syn_map = {k: sorted(v) for k, v in syn_map.items()}

    # 口语 → 文档用词 的改写表
    phrases = [[str(p[0]), str(p[1])] for p in (syn.get("phrases") or [])
               if isinstance(p, list) and len(p) >= 2]

    # 分词词表：规则词 + 同义词 + 分类名 + 标题里的高频词组
    lex = set()
    rules = (load_json(CONFIG_DIR / "classify_rules.json", {}) or {}).get("rules", {})
    for words in rules.values():
        lex.update(words)
    for k, vs in syn_map.items():
        lex.add(k)
        lex.update(vs)
    for p in phrases:
        lex.update(p[1].split())
    lex.update(categories())

    df = {}
    for d in docs:
        seen = set()
        for part in re.split(r"[^\w\u4e00-\u9fff]+", d["title"]):
            for n in (2, 3, 4):
                for i in range(len(part) - n + 1):
                    seen.add(part[i:i + n])
        for w in seen:
            df[w] = df.get(w, 0) + 1
    for w, c in df.items():
        if c >= 3:
            lex.add(w)

    lexicon = sorted({w for w in lex if 2 <= len(w) <= 6}, key=lambda w: (-len(w), w))[:5000]

    payload = {
        "generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "count": len(docs),
        "total_chars": sum(d["chars"] for d in docs),
        "categories": ordered,
        "cat_counts": seen_cats,
        "top_tags": [{"name": t, "count": c} for t, c in top_tags],
        "synonyms": syn_map,
        "phrases": phrases,
        "lexicon": lexicon,
        "docs": docs,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    (DATA_DIR / "index.js").write_text(
        "window.KB = " + json.dumps(payload, ensure_ascii=False) + ";\n",
        encoding="utf-8")

    print(f"已索引 {len(docs)} 篇文档 / 共 {payload['total_chars']:,} 字")
    print("分类分布：")
    for c in ordered:
        print(f"  - {c}: {seen_cats.get(c, 0)}")
    if errors:
        print("跳过/异常：")
        for e in errors:
            print("  !", e)
    print(f"输出：data/index.json 与 data/index.js（{payload['generated_at']}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
