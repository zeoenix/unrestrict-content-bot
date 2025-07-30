#!/usr/bin/env python3
"""
Absolute minimal server - no imports except built-ins
"""

import socket
import threading
import time
import os

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")

def handle_request(conn, addr):
    try:
        data = conn.recv(1024).decode()
        log(f"Request from {addr}: {data.split()[1] if len(data.split()) > 1 else 'UNKNOWN'}")
        
        if '/health' in data:
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nOK"
            log("✅ Health check response sent")
        else:
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nMinimal Server Running"
            log("✅ Default response sent")
            
        conn.send(response.encode())
    except Exception as e:
        log(f"❌ Request error: {e}")
    finally:
        conn.close()

def main():
    port = int(os.environ.get('PORT', 8080))
    log("🚀 MINIMAL SERVER STARTING")
    log(f"Port: {port}")
    
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind to all interfaces
        sock.bind(('0.0.0.0', port))
        log(f"✅ Socket bound to 0.0.0.0:{port}")
        
        # Listen
        sock.listen(5)
        log("✅ Socket listening (backlog: 5)")
        log("🎯 Server ready for connections")
        
        while True:
            try:
                conn, addr = sock.accept()
                # Handle in thread to avoid blocking
                thread = threading.Thread(target=handle_request, args=(conn, addr))
                thread.daemon = True
                thread.start()
            except Exception as e:
                log(f"❌ Accept error: {e}")
                
    except Exception as e:
        log(f"❌ Server failed: {e}")
        raise

if __name__ == "__main__":
    main()
