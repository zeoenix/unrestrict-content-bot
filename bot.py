# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
# 
# Enhanced & Modified By - @TP_Botz
# Security Improvements & Production Ready Version

import logging
import sys
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class Bot(Client):

    def __init__(self):
        try:
            super().__init__(
                "techvj_bot",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=BOT_TOKEN,
                plugins=dict(root="TechVJ"),
                workers=50,
                sleep_threshold=10
            )
            logger.info("Bot initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize bot: {e}")
            sys.exit(1)

    async def start(self):
        try:
            await super().start()
            me = await self.get_me()
            logger.info(f'Bot Started Successfully - @{me.username}')
            logger.info('Bot Powered By @VJ_Botz | Enhanced By @TP_Botz')
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
            sys.exit(1)

    async def stop(self, *args):
        try:
            await super().stop()
            logger.info('Bot Stopped Successfully')
        except Exception as e:
            logger.error(f"Error while stopping bot: {e}")

if __name__ == "__main__":
    try:
        bot = Bot()
        bot.run()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Critical error: {e}")
# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
# 
# Enhanced & Modified By - @TP_Botz
# Security Improvements & Production Ready Version
