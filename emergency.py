#!/usr/bin/env python3
"""
Emergency minimal server - no config dependencies
This will start no matter what and help us debug the issue
"""

import os
import sys
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class EmergencyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "healthy"})
            self.wfile.write(response.encode())
            
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({
                "status": "emergency_mode",
                "message": "Emergency server is running",
                "python_version": sys.version[:10],
                "port": os.environ.get("PORT", "8080")
            })
            self.wfile.write(response.encode())
            
        elif self.path == '/env':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Check environment variables safely
            env_check = {
                "PORT": os.environ.get("PORT", "Not set"),
                "BOT_TOKEN": "Set" if os.environ.get("BOT_TOKEN") else "Not set",
                "API_ID": "Set" if os.environ.get("API_ID") else "Not set",
                "API_HASH": "Set" if os.environ.get("API_HASH") else "Not set",
                "ADMINS": "Set" if os.environ.get("ADMINS") else "Not set",
                "DB_URI": "Set" if os.environ.get("DB_URI") else "Not set"
            }
            
            response = json.dumps(env_check, indent=2)
            self.wfile.write(response.encode())
            
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        print(f"[EMERGENCY] {format % args}")

def main():
    port = int(os.environ.get("PORT", 8080))
    
    print("🚨 EMERGENCY SERVER STARTING")
    print(f"Port: {port}")
    print(f"Python: {sys.version}")
    print(f"Working dir: {os.getcwd()}")
    
    try:
        server = HTTPServer(('0.0.0.0', port), EmergencyHandler)
        print(f"✅ Server bound to 0.0.0.0:{port}")
        print("🌐 Emergency server is running!")
        print(f"Health: http://0.0.0.0:{port}/health")
        print(f"Status: http://0.0.0.0:{port}/")
        print(f"Env check: http://0.0.0.0:{port}/env")
        
        server.serve_forever()
        
    except Exception as e:
        print(f"❌ EMERGENCY SERVER FAILED: {e}")
        import traceback
        print(traceback.format_exc())
        
        # Try a different approach - just print and stay alive
        print("🔄 Keeping process alive for debugging...")
        import time
        while True:
            print(f"Process still running... Port: {port}")
            time.sleep(30)

if __name__ == "__main__":
    main()
