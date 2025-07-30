#!/usr/bin/env python3
"""
Ultimate debugging server - will print everything to logs
"""

import os
import sys
import time
import socket
import subprocess

def log(message):
    """Print with timestamp"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")
    sys.stdout.flush()

def check_environment():
    """Check all environment variables"""
    log("=== ENVIRONMENT CHECK ===")
    log(f"Python version: {sys.version}")
    log(f"Platform: {sys.platform}")
    log(f"Working directory: {os.getcwd()}")
    log(f"User ID: {os.getuid() if hasattr(os, 'getuid') else 'N/A'}")
    
    # Check key environment variables
    env_vars = ['PORT', 'BOT_TOKEN', 'API_ID', 'API_HASH', 'ADMINS', 'DB_URI']
    for var in env_vars:
        value = os.environ.get(var, 'NOT SET')
        if var in ['BOT_TOKEN', 'API_HASH', 'DB_URI']:
            # Hide sensitive values
            display_value = f"SET ({len(value)} chars)" if value != 'NOT SET' else 'NOT SET'
        else:
            display_value = value
        log(f"{var}: {display_value}")

def check_network():
    """Check network connectivity"""
    log("=== NETWORK CHECK ===")
    port = int(os.environ.get('PORT', 8080))
    
    # Test port binding
    try:
        log(f"Testing port binding on {port}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port))
        log(f"✅ Successfully bound to 0.0.0.0:{port}")
        sock.close()
    except Exception as e:
        log(f"❌ Port binding failed: {e}")
        return False
    
    # Test different bind addresses
    for host in ['127.0.0.1', 'localhost', '0.0.0.0']:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind((host, port))
            log(f"✅ Can bind to {host}:{port}")
            sock.close()
        except Exception as e:
            log(f"❌ Cannot bind to {host}:{port} - {e}")
    
    return True

def start_simple_server():
    """Start the simplest possible HTTP server"""
    port = int(os.environ.get('PORT', 8080))
    
    log("=== STARTING SIMPLE SERVER ===")
    log(f"Attempting to start server on port {port}")
    
    try:
        # Use Python's built-in HTTP server
        import http.server
        import socketserver
        
        class MyHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                log(f"Received GET request: {self.path}")
                if self.path == '/health':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'healthy')
                    log("Sent health response")
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(b'server running')
                    log("Sent default response")
            
            def log_message(self, format, *args):
                log(f"HTTP: {format % args}")
        
        with socketserver.TCPServer(("0.0.0.0", port), MyHandler) as httpd:
            log(f"✅ Server started successfully on 0.0.0.0:{port}")
            log("Server is ready to accept connections")
            httpd.serve_forever()
            
    except Exception as e:
        log(f"❌ Server startup failed: {e}")
        import traceback
        log(f"Traceback: {traceback.format_exc()}")
        return False

def check_docker_environment():
    """Check Docker-specific environment"""
    log("=== DOCKER ENVIRONMENT CHECK ===")
    
    # Check if we're in Docker
    try:
        with open('/proc/1/cgroup', 'r') as f:
            content = f.read()
            if 'docker' in content:
                log("✅ Running inside Docker container")
            else:
                log("⚠️ Not running in Docker container")
    except:
        log("❓ Cannot determine if running in Docker")
    
    # Check network interfaces
    try:
        import subprocess
        result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
        log("Network interfaces:")
        for line in result.stdout.split('\n')[:10]:  # First 10 lines
            log(f"  {line}")
    except:
        log("Cannot check network interfaces")

def main():
    log("🚨 ULTIMATE DEBUG SERVER STARTING")
    log("=" * 50)
    
    # Run all checks
    check_environment()
    check_docker_environment()
    
    if not check_network():
        log("❌ Network check failed - staying alive for debugging")
        # Stay alive for 10 minutes for debugging
        for i in range(600):
            log(f"Process alive... {600-i} seconds remaining")
            time.sleep(1)
        return
    
    # Try to start server
    log("🚀 All checks passed, starting server...")
    start_simple_server()

if __name__ == "__main__":
    main()
