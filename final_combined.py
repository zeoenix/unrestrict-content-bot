#!/usr/bin/env python3
"""
Final combined server: Health check server + Telegram bot
"""

import os
import sys
import time
import threading
import logging
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HealthHandler(BaseHTTPRequestHandler):
    """Health check handler"""
    
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'healthy')
            logger.info("✅ Health check successful")
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>TechVJ Bot</h1><p>Status: Running</p>')
            logger.info("✅ Root endpoint accessed")
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Use our logger instead of default
        logger.info(f"HTTP: {format % args}")

def start_health_server():
    """Start the health check HTTP server in background thread"""
    port = int(os.environ.get('PORT', 8080))
    
    try:
        server = HTTPServer(('0.0.0.0', port), HealthHandler)
        logger.info(f"🏥 Health server running on port {port}")
        server.serve_forever()
    except Exception as e:
        logger.error(f"❌ Health server failed: {e}")
        raise

def start_telegram_bot():
    """Start the Telegram bot"""
    try:
        logger.info("🤖 Starting Telegram bot...")
        
        # Import and run the bot
        import bot
        
    except Exception as e:
        logger.error(f"❌ Bot startup failed: {e}")
        # Don't crash the health server if bot fails
        logger.info("⚠️ Bot failed but health server continues running")
        while True:
            time.sleep(60)  # Keep health server alive

def main():
    logger.info("🚀 FINAL COMBINED SERVER STARTING")
    logger.info("=" * 50)
    
    # Start health server in daemon thread
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()
    logger.info("✅ Health server thread started")
    
    # Give health server time to start
    time.sleep(2)
    
    # Start bot in main thread
    logger.info("🤖 Starting Telegram bot in main thread...")
    start_telegram_bot()

if __name__ == "__main__":
    main()
