#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从飞书 / Lark 知识库（Wiki）拉取文档。仅用标准库。

准备（飞书开放平台 open.feishu.cn 建自建应用）：
  1. 开通权限：wiki:wiki:readonly、docx:document:readonly、doc:readonly
  2. 发布版本后，把应用「添加为知识库成员（可阅读）」
  3. 拿到 App ID / App Secret

用法：
  set FEISHU_APP_ID=cli_xxx
  set FEISHU_APP_SECRET=xxx
  python tools/import_feishu.py --list
  python tools/import_feishu.py                      # 导入所有知识库
  python tools/import_feishu.py --space 客服手册      # 只导某个知识库
  python tools/import_feishu.py --doc doxcnxxxxx      # 导入单篇文档
  python tools/import_feishu.py --category 系统操作
"""
import os
import sys
import time
import json
import argparse
import urllib.request
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb_lib import write_doc, guess_category, strip_markdown, html_to_text

HOST = os.environ.get("FEISHU_HOST", "https://open.feishu.cn")
TOKEN = ""


def call(path, payload=None, method=None, params=""):
    url = HOST + path + (("?" + params) if params else "")
    data = None
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        method = method or "POST"
    req = urllib.request.Request(url, data=data, headers=headers, method=method or "GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")[:300]
        print(f"  ! {path} -> {e.code} {body}")
        return None
    except Exception as e:
        print(f"  ! 网络错误 {path}: {e}")
        return None


def login(app_id, app_secret):
    global TOKEN
    d = call("/open-apis/auth/v3/tenant_access_token/internal",
             {"app_id": app_id, "app_secret": app_secret})
    if not d or d.get("code") != 0:
        raise SystemExit(f"获取 tenant_access_token 失败：{d}")
    TOKEN = d["tenant_access_token"]
    print("飞书鉴权成功")


def list_spaces():
    out, token = [], ""
    while True:
        p = "page_size=50" + (f"&page_token={token}" if token else "")
        d = call("/open-apis/wiki/v2/spaces", params=p)
        if not d or d.get("code") != 0:
            print(f"  ! 读取知识库列表失败：{d}")
            return out
        data = d.get("data") or {}
        out.extend(data.get("items") or [])
        if not data.get("has_more"):
            break
        token = data.get("page_token") or ""
        if not token:
            break
    return out


def list_nodes(space_id, parent=""):
    out, token = [], ""
    while True:
        p = f"page_size=50&space_id={space_id}"
        if parent:
            p += f"&parent_node_token={parent}"
        if token:
            p += f"&page_token={token}"
        d = call(f"/open-apis/wiki/v2/spaces/{space_id}/nodes", params=p)
        if not d or d.get("code") != 0:
            break
        data = d.get("data") or {}
        out.extend(data.get("items") or [])
        if not data.get("has_more"):
            break
        token = data.get("page_token") or ""
        if not token:
            break
        time.sleep(0.2)
    return out


def fetch_doc(obj_token, obj_type):
    if obj_type == "docx":
        d = call(f"/open-apis/docx/v1/documents/{obj_token}/raw_content")
        if d and d.get("code") == 0:
            return (d.get("data") or {}).get("content") or ""
        return ""
    if obj_type == "doc":
        d = call(f"/open-apis/doc/v2/{obj_token}/raw_content")
        if d and d.get("code") == 0:
            return (d.get("data") or {}).get("content") or ""
        d = call(f"/open-apis/doc/v2/{obj_token}/content")
        if d and d.get("code") == 0:
            return html_to_text((d.get("data") or {}).get("content") or "")
        return ""
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--app-id", default=os.environ.get("FEISHU_APP_ID", ""))
    ap.add_argument("--app-secret", default=os.environ.get("FEISHU_APP_SECRET", ""))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--space", default="", help="知识库名称包含该词")
    ap.add_argument("--doc", default="", help="直接导入单个文档 token")
    ap.add_argument("--category", default="")
    ap.add_argument("--limit", type=int, default=500)
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()

    if not args.app_id or not args.app_secret:
        raise SystemExit("缺少凭据：set FEISHU_APP_ID=cli_xxx 和 set FEISHU_APP_SECRET=xxx")

    login(args.app_id, args.app_secret)

    # 单篇模式
    if args.doc:
        body = fetch_doc(args.doc, "docx") or fetch_doc(args.doc, "doc")
        if not body:
            raise SystemExit("没取到内容，检查文档 token 与应用权限。")
        cat = args.category or guess_category("", strip_markdown(body))[0]
        write_doc(title=f"飞书文档-{args.doc[:8]}", body=body, category=cat,
                  source="飞书", url=f"https://feishu.cn/docx/{args.doc}")
        print(f"已导入 1 篇 → {cat}")
        return 0

    spaces = list_spaces()
    if args.space:
        spaces = [s for s in spaces if args.space in (s.get("name") or "")]
    if not spaces:
        raise SystemExit("没有可见知识库。请确认应用已被添加为知识库成员。")

    print(f"共 {len(spaces)} 个知识库：")
    for s in spaces:
        print(f"  - {s.get('name')}  [{s.get('space_id')}]")
    if args.list:
        return 0

    total = 0
    for s in spaces:
        sid, sname = s.get("space_id"), s.get("name") or "飞书知识库"
        print(f"\n== 导入：{sname}")
        queue = [("", 0)]
        seen_nodes = set()
        while queue:
            parent, depth = queue.pop(0)
            if depth > 6:
                continue
            for n in list_nodes(sid, parent):
                nt = n.get("node_token")
                if not nt or nt in seen_nodes:
                    continue
                seen_nodes.add(nt)
                if n.get("has_child"):
                    queue.append((nt, depth + 1))
                if total >= args.limit:
                    print(f"达到 --limit {args.limit}，停止。")
                    return 0
                obj_type = n.get("obj_type")
                obj_token = n.get("obj_token")
                title = (n.get("title") or "").strip() or "未命名"
                if obj_type not in ("docx", "doc"):
                    print(f"  - 跳过（{obj_type} 类型暂不支持）：{title}")
                    continue
                body = fetch_doc(obj_token, obj_type)
                if not body.strip():
                    print(f"  - 跳过（空/无权限）：{title}")
                    continue
                cat = args.category or guess_category(title, strip_markdown(body))[0]
                write_doc(title=title, body=body, category=cat,
                          tags=[sname], source="飞书",
                          url=f"https://feishu.cn/wiki/{nt}",
                          extra_meta={"book": sname})
                total += 1
                print(f"  [{total}] {title}  →  {cat}")
                time.sleep(args.sleep)

    print(f"\n完成：共导入 {total} 篇。下一步：python tools/build_index.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
