#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""公共工具函数：路径、slug、HTML 转文本、docx 提取、写文档。全部只用标准库。"""
import re
import os
import json
import hashlib
import zipfile
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # kb/
DOCS_DIR = ROOT / "docs"
IMPORT_DIR = ROOT / "imported"
DATA_DIR = ROOT / "data"
CONFIG_DIR = ROOT / "config"

BAD_CHARS = re.compile(r'[\\/:*?"<>|\r\n\t]+')


def now_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def load_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return default


def categories():
    cfg = load_json(CONFIG_DIR / "categories.json", {}) or {}
    return cfg.get("categories", [])


def slugify(text, maxlen=60):
    """生成安全的文件名片段，保留中文。"""
    text = (text or "").strip()
    text = BAD_CHARS.sub(" ", text)
    text = re.sub(r"\s+", "-", text).strip("-.")
    text = text.replace("#", "").replace("*", "").replace("`", "")
    if len(text) > maxlen:
        text = text[:maxlen].rstrip("-")
    return text or "untitled"


def short_hash(text):
    return hashlib.md5((text or "").encode("utf-8")).hexdigest()[:6]


# ---------------- HTML -> 纯文本 / Markdown ----------------

def html_to_text(html):
    """粗暴但够用的 HTML 转纯文本（不依赖 bs4）。"""
    if not html:
        return ""
    s = html
    s = re.sub(r"(?is)<(script|style|noscript|svg|iframe)[^>]*>.*?</\1>", " ", s)
    # 表格换行处理
    s = re.sub(r"(?i)</t[dh]>", "\t", s)
    s = re.sub(r"(?i)</tr>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    # 块级元素前后换行
    s = re.sub(r"(?i)</?(p|div|section|article|h[1-6]|li|ul|ol|blockquote|pre|table|thead|tbody)[^>]*>", "\n", s)
    s = re.sub(r"(?is)<h1[^>]*>", "\n# ", s)
    s = re.sub(r"(?is)<h2[^>]*>", "\n## ", s)
    s = re.sub(r"(?is)<h3[^>]*>", "\n### ", s)
    s = re.sub(r"(?is)<(b|strong)[^>]*>", "**", s)
    s = re.sub(r"(?is)</(b|strong)>", "**", s)
    s = re.sub(r"(?is)<(i|em)[^>]*>", "*", s)
    s = re.sub(r"(?is)</(i|em)>", "*", s)
    s = re.sub(r"(?is)<li[^>]*>", "\n- ", s)
    s = re.sub(r"(?is)<a[^>]*href=[\"']([^\"']+)[\"'][^>]*>", r"[", s)
    s = re.sub(r"(?is)</a>", "]", s)
    # 去掉剩下的标签
    s = re.sub(r"(?s)<[^>]+>", "", s)
    # 实体
    entities = {
        "&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">",
        "&quot;": '"', "&#39;": "'", "&ldquo;": "“", "&rdquo;": "”",
        "&mdash;": "—", "&hellip;": "…", "&times;": "×",
    }
    for k, v in entities.items():
        s = s.replace(k, v)
    s = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), s)
    # 清理空白
    s = re.sub(r"[ \t\u00a0]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    lines = [ln.strip() for ln in s.splitlines()]
    return "\n".join(ln for ln in lines if ln).strip()


def markdown_escape(text):
    return text


def strip_markdown(md):
    """把 Markdown 转成用于搜索/摘要的纯文本。"""
    s = md or ""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    # 去掉语雀正文里残留的内联 HTML（<font style="color:#xxx"> 之类）
    s = re.sub(r"(?s)</?[a-zA-Z][a-zA-Z0-9]{0,10}(?:\s[^>]{0,300})?>", "", s)
    s = re.sub(r"(?s)```.*?```", " ", s)
    s = re.sub(r"(?m)^\s*\|.*\|\s*$", lambda m: " ".join(
        c.strip() for c in m.group(0).strip().strip("|").split("|")), s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", s)
    s = re.sub(r"(?m)^\s{0,3}>\s?", "", s)
    s = re.sub(r"(\*\*|__|\*|_|`|~~)", "", s)
    s = re.sub(r"(?m)^\s*[-*+]\s+", "· ", s)
    s = re.sub(r"(?m)^\s*---+\s*$", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


# ---------------- docx 提取（zipfile + 正则） ----------------

def docx_to_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
    except Exception as e:
        return ""
    xml = re.sub(r"(?s)<w:tab[^>]*/>", "\t", xml)
    xml = re.sub(r"(?s)</w:p>", "\n", xml)
    xml = re.sub(r"(?s)<[^>]+>", "", xml)
    xml = (xml.replace("&lt;", "<").replace("&gt;", ">")
              .replace("&amp;", "&").replace("&quot;", '"'))
    xml = re.sub(r"\n{3,}", "\n\n", xml)
    return xml.strip()


# ---------------- 写文档 ----------------

VALID_EXT_TEXT = {".md", ".markdown", ".txt", ".html", ".htm", ".docx"}


def write_doc(title, body, category="其他", tags=None, source="手工",
              url="", updated=None, extra_meta=None, subdir=None):
    """写一个带 front matter 的 markdown 文档，返回 Path。重名自动加后缀。"""
    title = (title or "未命名").strip().replace("\n", " ")[:120]
    tags = [t.strip() for t in (tags or []) if t and t.strip()]
    out_dir = DOCS_DIR / (subdir or slugify(category))
    out_dir.mkdir(parents=True, exist_ok=True)

    base = slugify(title)
    path = out_dir / f"{base}.md"
    if path.exists():
        path = out_dir / f"{base}-{short_hash(url or title)}.md"
    n = 2
    while path.exists():
        path = out_dir / f"{base}-{n}.md"
        n += 1

    fm = ["---",
          f"title: {title}",
          f"category: {category}",
          f"tags: {', '.join(tags)}",
          f"source: {source}",
          f"updated: {updated or now_str()}"]
    if url:
        fm.append(f"url: {url}")
    for k, v in (extra_meta or {}).items():
        if v not in (None, ""):
            fm.append(f"{k}: {v}")
    fm.append("---")

    content = "\n".join(fm) + "\n\n" + (body or "").strip() + "\n"
    path.write_text(content, encoding="utf-8")
    return path


def print_ok(msg):
    print(f"[OK] {msg}")


# ---------------- 自动归类 ----------------

_RULES_CACHE = None


def _rules():
    global _RULES_CACHE
    if _RULES_CACHE is None:
        cfg = load_json(CONFIG_DIR / "classify_rules.json", {}) or {}
        _RULES_CACHE = (cfg.get("rules", {}), float(cfg.get("threshold", 3)))
    return _RULES_CACHE


def guess_category(title, body, default="其他"):
    """按关键词打分返回分类名；分数不够则返回 default。返回 (category, scores)。"""
    rules, threshold = _rules()
    title = title or ""
    body = body or ""
    # 正文太长时只取前 4000 字，避免长文档被某个词刷分
    sample = body[:4000]
    scores = {}
    for cat, words in rules.items():
        score = 0
        for w in words:
            if not w:
                continue
            score += title.count(w) * 3
            score += min(sample.count(w), 6)
        if score:
            scores[cat] = score
    if not scores:
        return default, scores
    best = max(scores.items(), key=lambda kv: kv[1])
    if best[1] < threshold:
        return default, scores
    return best[0], scores
