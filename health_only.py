#!/usr/bin/env python3
"""
Simple health-only server - separates health checks from bot completely
"""

import os
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class HealthHandler(BaseHTTPRequestHandler):
    """Minimal health check handler"""
    
    def do_GET(self):
        logger.info(f"Health check request: {self.path}")
        
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            self.wfile.write(b'OK')
            logger.info("✅ Health check: OK")
            
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>TechVJ Bot Health Server</h1><p>Status: Running</p>')
            logger.info("✅ Root check: OK")
            
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
            logger.info(f"❌ Not found: {self.path}")
    
    def log_message(self, format, *args):
        # Custom logging to avoid duplicate messages
        logger.info(f"HTTP: {format % args}")

def main():
    port = int(os.environ.get('PORT', 8080))
    
    logger.info("🏥 Starting Health-Only Server")
    logger.info("=" * 40)
    logger.info(f"Port: {port}")
    logger.info(f"Endpoints: /health, /")
    
    try:
        server = HTTPServer(('0.0.0.0', port), HealthHandler)
        logger.info(f"✅ Server bound to 0.0.0.0:{port}")
        logger.info("🚀 Server starting...")
        
        server.serve_forever()
        
    except Exception as e:
        logger.error(f"❌ Server failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise

if __name__ == "__main__":
    main()
