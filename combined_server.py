#!/usr/bin/env python3
"""
Combined server: Runs both the Telegram bot AND health check server
"""

import os
import sys
import time
import threading
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HealthHandler(BaseHTTPRequestHandler):
    """Simple health check handler"""
    
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'healthy')
            logger.info("Health check successful")
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'TechVJ Bot Server Running')
            logger.info("Root endpoint accessed")
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress default HTTP logging to avoid clutter
        pass

def start_health_server():
    """Start the health check HTTP server"""
    port = int(os.environ.get('PORT', 8080))
    
    try:
        server = HTTPServer(('0.0.0.0', port), HealthHandler)
        logger.info(f"🏥 Health server starting on port {port}")
        server.serve_forever()
    except Exception as e:
        logger.error(f"❌ Health server failed: {e}")
        raise

def start_telegram_bot():
    """Start the Telegram bot"""
    try:
        logger.info("🤖 Starting Telegram bot...")
        
        # Import and run the bot
        import bot  # This will start the bot
        
    except Exception as e:
        logger.error(f"❌ Bot startup failed: {e}")
        raise

def main():
    logger.info("🚀 Combined Server Starting...")
    logger.info("=" * 50)
    
    # Start health server in a separate thread
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()
    logger.info("✅ Health server thread started")
    
    # Give health server a moment to start
    time.sleep(2)
    
    # Start the Telegram bot (main thread)
    logger.info("🤖 Starting bot in main thread...")
    start_telegram_bot()

if __name__ == "__main__":
    main()
