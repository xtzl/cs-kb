#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布前脱敏：把文档里的真实口令/密钥替换成占位符，保留句子结构。

用法：
  python tools/redact_secrets.py --dry-run     # 只列出会改什么
  python tools/redact_secrets.py               # 实际改写

处理原则：
  - 只打码「值」，不动「说明」，客服仍知道这里有个密码、要找运维要
  - 账号/用户名保留（不是秘密，客服要照着填）
  - 微信/企业微信的 AppID 保留，AppSecret 打码
"""
import re
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import DOCS_DIR

PLACEHOLDER = "****（已脱敏，请向运维索取）"

# 1) 云厂商密钥：整串替换
HARD_PATTERNS = [
    (re.compile(r"LTAI[0-9A-Za-z]{10,}"), "LTAI****已脱敏"),
    (re.compile(r"AKIA[0-9A-Z]{12,}"), "AKIA****已脱敏"),
    (re.compile(r"(?i)(AccessKey\s*Secret\s*[:：]\s*)[A-Za-z0-9/+=]{8,}"), r"\1" + PLACEHOLDER),
    (re.compile(r"(?i)(AccessKey\s*ID\s*[:：]\s*)LTAI[0-9A-Za-z]{10,}"), r"\1LTAI****已脱敏"),
    # 百度网盘提取码
    (re.compile(r"([?&]pwd=)([A-Za-z0-9]{2,10})"), r"\1****"),
    # SQL 里写死的密码
    (re.compile(r"(?i)(Password\s*=\s*')[^']{3,}(')"), r"\1****已脱敏\2"),
    # 连接串里的密码
    (re.compile(r"(?i)(password=)[^;，,\s]{2,}(?=[;,;\s]|$)"), r"\1****已脱敏"),
    # sqlcmd / mysql 命令行里的口令参数：-P xxx
    (re.compile(r"(\s-P\s+)(?!\*)[^\s,;]{3,40}"), r"\1" + PLACEHOLDER),
]

# 2) 中文语境：密码/口令/密钥 后面跟的具体值
KEYWORD = re.compile(r"(密码|口令|密钥|秘钥|password|passwd|pwd|secret)", re.I)
LEAD = re.compile(r"^(?:\s*(?:默认为|默认为|默认|为|是|设为|设置为|填写|填|输入|统一为|均为|：|:|=))+\s*")
VALUE = re.compile(r"[A-Za-z0-9!@#$%^&*._+\-]{4,60}")

# 不是秘密、不该打码的常见词
ALLOW = {
    "administrator", "admin", "root", "sa", "none", "null", "http", "https",
    "www", "com", "cn", "sdk2", "password", "passwd", "pwd", "secret", "token",
    "true", "false", "yes", "no", "ok", "id", "ip", "url", "appid",
    "android", "ios", "windows", "server", "client", "default",
}


def redact_line(line: str):
    """处理一行，返回 (新行, 是否改动)。"""
    orig = line

    for pat, rep in HARD_PATTERNS:
        line = pat.sub(rep, line)

    # 关键字后面的值（不要求分隔符，兼容「登录密码 Ych123456」「输入密码1或4009999261」）
    out = []
    pos = 0
    for m in KEYWORD.finditer(line):
        if m.start() < pos:
            continue
        window = line[m.end():m.end() + 16]
        vm = VALUE.search(window)
        if not vm:
            continue
        val = vm.group(0)
        # 全是星号 = 已处理过；中文/纯英文说明文字不算
        if val.strip("*") == "" or val.lower() in ALLOW or "已脱敏" in val:
            continue
        if not re.search(r"[0-9!@#$%^&*._+\-]", val):
            continue
        start = m.end() + vm.start()
        if start < pos:
            continue
        out.append(line[pos:start])
        out.append(PLACEHOLDER)
        pos = start + len(val)
    if out:
        out.append(line[pos:])
        line = "".join(out)

    return line, line != orig


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    files = sorted(DOCS_DIR.rglob("*.md"))
    changed_files = 0
    changed_lines = 0
    samples = []

    for p in files:
        text = p.read_text(encoding="utf-8")
        lines = text.split("\n")
        dirty = False
        for i, ln in enumerate(lines):
            new, hit = redact_line(ln)
            if hit:
                lines[i] = new
                dirty = True
                changed_lines += 1
                if len(samples) < 12:
                    samples.append((p.name, ln.strip()[:80], new.strip()[:80]))
        if dirty:
            changed_files += 1
            if not args.dry_run:
                p.write_text("\n".join(lines), encoding="utf-8")
            if args.limit and changed_files >= args.limit:
                break

    print(f"{'将修改' if args.dry_run else '已修改'} {changed_files} 个文件、{changed_lines} 行")
    for name, before, after in samples:
        print(f"\n  {name}")
        print(f"    - {before}")
        print(f"    + {after}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
