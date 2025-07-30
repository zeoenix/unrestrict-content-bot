#!/usr/bin/env python3
"""
Ultra simple diagnostic - prints and exits immediately
"""

import os
import sys

print("=" * 60)
print("🚨 EMERGENCY DIAGNOSTIC")
print("=" * 60)
print(f"Python: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Working dir: {os.getcwd()}")

# Check PORT
port = os.environ.get('PORT', 'NOT_SET')
print(f"PORT env var: {port}")

# List files
try:
    files = os.listdir('.')
    print(f"Files: {files}")
except Exception as e:
    print(f"File list error: {e}")

# Test socket
try:
    import socket
    port_int = int(port) if port != 'NOT_SET' else 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port_int))
    print(f"✅ Port {port_int} binding SUCCESS")
    sock.close()
except Exception as e:
    print(f"❌ Port binding FAILED: {e}")

print("🔍 Diagnostic complete - staying alive for 2 minutes")

# Stay alive briefly
import time
for i in range(24):  # 2 minutes
    print(f"Alive: {24-i} cycles remaining")
    time.sleep(5)

print("🏁 Exiting")
