#!/usr/bin/env python3
"""
Combined startup script - runs both health server and bot
"""

import subprocess
import time
import threading
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_health_server():
    """Start the health server in background"""
    try:
        logger.info("🏥 Starting health server...")
        # Start health server as subprocess
        process = subprocess.Popen(
            ["python", "minimal_server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        # Monitor health server output
        if process.stdout:
            for line in process.stdout:
                logger.info(f"HEALTH: {line.strip()}")
        else:
            logger.info("HEALTH: Server started (no stdout)")
            
    except Exception as e:
        logger.error(f"❌ Health server failed: {e}")

def start_bot():
    """Start the bot"""
    try:
        logger.info("🤖 Starting Telegram bot...")
        # Give health server time to start
        time.sleep(3)
        
        # Start bot (this will block)
        subprocess.run(["python", "bot.py"])
        
    except Exception as e:
        logger.error(f"❌ Bot failed: {e}")

def main():
    logger.info("🚀 COMBINED STARTUP STARTING")
    
    # Start health server in background thread
    health_thread = threading.Thread(target=start_health_server, daemon=True)
    health_thread.start()
    logger.info("✅ Health server thread started")
    
    # Start bot in main thread (blocking)
    start_bot()

if __name__ == "__main__":
    main()
