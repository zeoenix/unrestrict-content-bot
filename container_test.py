#!/usr/bin/env python3
"""
Ultra minimal test - just print and exit
"""

import os
import sys

def main():
    port = os.environ.get('PORT', '8080')
    print(f"🚀 CONTAINER STARTING")
    print(f"Python version: {sys.version}")
    print(f"Port from env: {port}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}")
    
    # Try to import socket
    try:
        import socket
        print("✅ Socket module available")
    except Exception as e:
        print(f"❌ Socket import failed: {e}")
        sys.exit(1)
    
    # Try to bind to port
    try:
        port_int = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', port_int))
        print(f"✅ Successfully bound to port {port_int}")
        sock.close()
    except Exception as e:
        print(f"❌ Port binding failed: {e}")
        sys.exit(1)
    
    print("🎯 Container startup successful - exiting for testing")
    return 0

if __name__ == "__main__":
    main()
