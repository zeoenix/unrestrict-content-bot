import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("BOT_TOKEN environment variable is required!")
    raise ValueError("BOT_TOKEN environment variable is required!")

# Your API ID from my.telegram.org
api_id_str = os.environ.get("API_ID")
if not api_id_str:
    logger.error("API_ID environment variable is required!")
    raise ValueError("API_ID environment variable is required!")
try:
    API_ID = int(api_id_str)
except ValueError:
    logger.error("API_ID must be a valid integer!")
    raise ValueError("API_ID must be a valid integer!")

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH")
if not API_HASH:
    logger.error("API_HASH environment variable is required!")
    raise ValueError("API_HASH environment variable is required!")

# Your Owner / Admin Id For Broadcast 
admins_str = os.environ.get("ADMINS")
if not admins_str:
    logger.error("ADMINS environment variable is required!")
    raise ValueError("ADMINS environment variable is required!")
try:
    ADMINS = int(admins_str)
except ValueError:
    logger.error("ADMINS must be a valid integer!")
    raise ValueError("ADMINS must be a valid integer!")

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI")
if not DB_URI:
    logger.error("DB_URI environment variable is required!")
    raise ValueError("DB_URI environment variable is required!")

DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = os.environ.get('ERROR_MESSAGE', 'True').lower() in ['true', '1', 'yes']

# Session string size validation
SESSION_STRING_SIZE = 351

# Rate limiting settings
RATE_LIMIT_DELAY = 3  # seconds between requests
