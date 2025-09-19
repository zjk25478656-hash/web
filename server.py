#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
悠悠18岁生日纪念网站 - 本地测试服务器
用于本地开发和测试网站功能

使用方法：
python server.py

然后访问：http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import sys
import os

# 服务器配置
PORT = 8000
HOST = 'localhost'

# 切换到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头，允许本地开发
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.log_date_time_string()}] {format % args}")

def start_server():
    """启动本地开发服务器"""
    try:
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            url = f"http://{HOST}:{PORT}"
            
            print("=" * 50)
            print("🎂 悠悠18岁生日纪念网站 - 本地服务器")
            print("=" * 50)
            print(f"🌐 服务器地址: {url}")
            print(f"📁 服务目录: {os.getcwd()}")
            print("🔧 按 Ctrl+C 停止服务器")
            print("=" * 50)
            
            # 自动打开浏览器
            try:
                webbrowser.open(url)
                print("🚀 已自动打开浏览器")
            except:
                print(f"请手动打开浏览器访问: {url}")
            
            print("\n⏰ 服务器运行中...")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n👋 服务器已停止")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口")
            print(f"或者杀死占用端口的进程：lsof -ti:{PORT} | xargs kill -9")
        else:
            print(f"❌ 启动服务器失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()