#!/usr/bin/env python3
"""
Minimal health check server for deployment
No dependencies except built-in Python modules
"""

import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import subprocess
import time

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "healthy"})
            self.wfile.write(response.encode())
        elif self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'pong')
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({
                "status": "running",
                "service": "TechVJ Save Content Bot",
                "message": "Health check server is running"
            })
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        print(f"Health server: {format % args}")

def start_bot():
    """Start the bot after a delay"""
    time.sleep(10)  # Wait for health server to be fully ready
    try:
        print("🤖 Starting Telegram bot...")
        subprocess.Popen(["python", "bot.py"])
        print("✅ Bot started in background")
    except Exception as e:
        print(f"❌ Bot startup error: {e}")

def main():
    port = int(os.environ.get("PORT", 8080))
    
    # Start bot in background thread
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    
    # Start minimal HTTP server
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    print(f"🌐 Health server starting on port {port}")
    print(f"Health check available at: http://0.0.0.0:{port}/health")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
        server.shutdown()

if __name__ == "__main__":
    main()
