#!/usr/bin/env python3
"""
Simple HTTP server using Python's built-in server
"""

import os
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SimpleHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler"""
    
    def do_GET(self):
        logger.info(f"Received request: {self.path}")
        
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'healthy')
            logger.info("✅ Health check successful")
            
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Server is running')
            logger.info("✅ Root endpoint accessed")
            
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found')
    
    def log_message(self, format, *args):
        logger.info(f"HTTP: {format % args}")

def main():
    port = int(os.environ.get('PORT', 8080))
    
    logger.info("🏥 Starting Simple HTTP Server")
    logger.info(f"Port: {port}")
    
    try:
        server = HTTPServer(('0.0.0.0', port), SimpleHandler)
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
