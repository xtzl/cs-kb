# -*- coding: utf-8 -*-
"""扫描文档里的明文密钥，输出命中位置。"""
import re
import pathlib

ROOT = pathlib.Path("C:/Users/Administrator/WorkBuddy/2026-11-12-20-40-42/kb/docs")
PATTERNS = [
    ("阿里云 AccessKey", re.compile(r"LTAI[0-9A-Za-z]{12,}")),
    ("AccessKey Secret 字段", re.compile(r"(?i)access\s*key\s*secret\s*[:：]\s*([A-Za-z0-9]{16,})")),
    ("AWS AK", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("疑似密码行", re.compile(r"(?i)(密码|password|passwd|pwd)\s*[:：=]\s*([^\s，。；,;]{6,30})")),
    ("疑似 token 行", re.compile(r"(?i)(token|secret)\s*[:：=]\s*([A-Za-z0-9_\-]{20,})")),
]

hits = []
for p in ROOT.rglob("*.md"):
    t = p.read_text(encoding="utf-8", errors="ignore")
    for name, pat in PATTERNS:
        for m in pat.finditer(t):
            line_no = t[:m.start()].count("\n") + 1
            snippet = t[max(0, m.start() - 30):m.end() + 10].replace("\n", " ")
            hits.append((p.relative_to(ROOT).as_posix(), line_no, name, snippet))

print(f"命中 {len(hits)} 处：")
for f, ln, name, s in hits[:60]:
    print(f"  [{name}] {f}:{ln}")
    print(f"      ...{s}...")
