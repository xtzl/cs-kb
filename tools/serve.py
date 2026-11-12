#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地启动知识库搜索界面。python tools/serve.py

只监听 127.0.0.1，外部网络访问不到。按 Ctrl+C 关闭。
"""
import sys
import os
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(os.environ.get("KB_PORT", "8765"))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # 静音访问日志


def main():
    url = f"http://127.0.0.1:{PORT}/index.html"
    if not (ROOT / "data" / "index.js").exists():
        print("提示：还没生成索引，先运行 python tools/build_index.py")
    httpd = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"知识库已启动：{url}")
    print("按 Ctrl+C 停止。")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n已停止。")
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
