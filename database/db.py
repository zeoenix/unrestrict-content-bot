import motor.motor_asyncio
import logging
from typing import Optional, Dict, Any
from config import DB_NAME, DB_URI

logger = logging.getLogger(__name__)

class Database:
    
    def __init__(self, uri: str, database_name: str):
        try:
            self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
            self.db = self._client[database_name]
            self.col = self.db.users
            logger.info(f"Database connected successfully to {database_name}")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def new_user(self, id: int, name: str) -> Dict[str, Any]:
        return dict(
            id=id,
            name=name,
            session=None,
        )
    
    async def add_user(self, id: int, name: str) -> bool:
        try:
            user = self.new_user(id, name)
            await self.col.insert_one(user)
            logger.info(f"User {id} added successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to add user {id}: {e}")
            return False
    
    async def is_user_exist(self, id: int) -> bool:
        try:
            user = await self.col.find_one({'id': int(id)})
            return bool(user)
        except Exception as e:
            logger.error(f"Error checking if user {id} exists: {e}")
            return False
    
    async def total_users_count(self) -> int:
        try:
            count = await self.col.count_documents({})
            return count
        except Exception as e:
            logger.error(f"Error getting total users count: {e}")
            return 0

    async def get_all_users(self):
        try:
            return self.col.find({})
        except Exception as e:
            logger.error(f"Error getting all users: {e}")
            return []

    async def delete_user(self, user_id: int) -> bool:
        try:
            result = await self.col.delete_many({'id': int(user_id)})
            logger.info(f"Deleted {result.deleted_count} records for user {user_id}")
            return result.deleted_count > 0
        except Exception as e:
            logger.error(f"Error deleting user {user_id}: {e}")
            return False

    async def set_session(self, id: int, session: Optional[str]) -> bool:
        try:
            await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})
            logger.info(f"Session updated for user {id}")
            return True
        except Exception as e:
            logger.error(f"Error setting session for user {id}: {e}")
            return False

    async def get_session(self, id: int) -> Optional[str]:
        try:
            user = await self.col.find_one({'id': int(id)})
            if user:
                return user.get('session')
            return None
        except Exception as e:
            logger.error(f"Error getting session for user {id}: {e}")
            return None

# Initialize database connection
try:
    if not DB_URI:
        raise ValueError("DB_URI is required")
    db = Database(DB_URI, DB_NAME)
except Exception as e:
    logger.critical(f"Failed to initialize database: {e}")
    raise
