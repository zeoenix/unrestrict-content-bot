#!/usr/bin/env python3
"""
Diagnostic server to debug deployment issues
This will help us see what's happening during startup
"""

import os
import sys
import json
import traceback
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

class DiagnosticHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == '/health':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({
                    "status": "healthy",
                    "timestamp": str(__import__('time').time()),
                    "python_version": sys.version,
                    "port": os.environ.get("PORT", "8080")
                })
                self.wfile.write(response.encode())
                
            elif self.path == '/debug':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # Collect debug info
                debug_info = {
                    "environment_variables": dict(os.environ),
                    "python_path": sys.path,
                    "working_directory": os.getcwd(),
                    "files_in_directory": os.listdir('.'),
                    "port": os.environ.get("PORT", "8080"),
                    "python_version": sys.version,
                    "platform": sys.platform
                }
                
                response = json.dumps(debug_info, indent=2)
                self.wfile.write(response.encode())
                
            elif self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({
                    "status": "running",
                    "service": "TechVJ Diagnostic Server",
                    "message": "Server is responding",
                    "endpoints": ["/health", "/debug", "/test-config"]
                })
                self.wfile.write(response.encode())
                
            elif self.path == '/test-config':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                # Test configuration loading
                config_status = {}
                try:
                    from config import BOT_TOKEN, API_ID, API_HASH, ADMINS, DB_URI
                    config_status = {
                        "config_loaded": True,
                        "bot_token_exists": bool(BOT_TOKEN),
                        "api_id_exists": bool(API_ID),
                        "api_hash_exists": bool(API_HASH),
                        "admins_exists": bool(ADMINS),
                        "db_uri_exists": bool(DB_URI)
                    }
                except Exception as e:
                    config_status = {
                        "config_loaded": False,
                        "error": str(e),
                        "traceback": traceback.format_exc()
                    }
                
                response = json.dumps(config_status, indent=2)
                self.wfile.write(response.encode())
                
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"error": "Not found"})
                self.wfile.write(response.encode())
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({
                "error": str(e),
                "traceback": traceback.format_exc()
            })
            self.wfile.write(response.encode())
    
    def log_message(self, format, *args):
        print(f"[DIAGNOSTIC] {format % args}")

def test_port_binding():
    """Test if we can bind to the port"""
    port = int(os.environ.get("PORT", 8080))
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.close()
        print(f"✅ Port {port} is available")
        return True
    except Exception as e:
        print(f"❌ Port {port} binding failed: {e}")
        return False

def main():
    print("🔍 Starting diagnostic server...")
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Environment PORT: {os.environ.get('PORT', 'Not set')}")
    
    # Test port binding
    port = int(os.environ.get("PORT", 8080))
    print(f"Testing port {port}...")
    
    if not test_port_binding():
        print("❌ Port binding test failed!")
        sys.exit(1)
    
    try:
        server = HTTPServer(('0.0.0.0', port), DiagnosticHandler)
        print(f"🌐 Diagnostic server starting on 0.0.0.0:{port}")
        print(f"Health check: http://0.0.0.0:{port}/health")
        print(f"Debug info: http://0.0.0.0:{port}/debug")
        print(f"Config test: http://0.0.0.0:{port}/test-config")
        
        server.serve_forever()
        
    except Exception as e:
        print(f"❌ Server startup failed: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    main()
