import os
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_env_var(var_name, required=True, default=None):
    """Safely get environment variable without crashing"""
    value = os.environ.get(var_name, default)
    if required and not value:
        logger.error(f"{var_name} environment variable is required but not set!")
        return None
    return value

# Bot token @Botfather
BOT_TOKEN = get_env_var("BOT_TOKEN", required=True)

# Your API ID from my.telegram.org
api_id_str = get_env_var("API_ID", required=True)
try:
    API_ID = int(api_id_str) if api_id_str else None
except (ValueError, TypeError):
    logger.error("API_ID must be a valid integer!")
    API_ID = None

# Your API Hash from my.telegram.org
API_HASH = get_env_var("API_HASH", required=True)

# Your Owner / Admin Id For Broadcast 
admins_str = get_env_var("ADMINS", required=True)
try:
    ADMINS = int(admins_str) if admins_str else None
except (ValueError, TypeError):
    logger.error("ADMINS must be a valid integer!")
    ADMINS = None

# Your Mongodb Database Url
DB_URI = get_env_var("DB_URI", required=True)

# Database name
DB_NAME = get_env_var("DB_NAME", required=False, default="vjsavecontentbot")

# Error message flag
error_msg_str = get_env_var("ERROR_MESSAGE", required=False, default="True")
ERROR_MESSAGE = error_msg_str.lower() == "true" if error_msg_str else True

# Log configuration status
def validate_config():
    """Validate configuration without crashing"""
    issues = []
    
    if not BOT_TOKEN:
        issues.append("BOT_TOKEN not set")
    if not API_ID:
        issues.append("API_ID not set or invalid")
    if not API_HASH:
        issues.append("API_HASH not set")
    if not ADMINS:
        issues.append("ADMINS not set or invalid")
    if not DB_URI:
        issues.append("DB_URI not set")
    
    if issues:
        logger.error(f"Configuration issues: {', '.join(issues)}")
        return False
    
    logger.info("Configuration validated successfully")
    return True

# Don't crash on import, just log issues
if __name__ == "__main__":
    validate_config()
