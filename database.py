# database.py
from pyrogram import Client, enums
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, DEFAULT_CONFIG, DEFAULT_PUNISHMENT, DEFAULT_WARNING_LIMIT

mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client['telegram_bot_db']
warnings_collection = db['warnings']
punishments_collection = db['punishments']
whitelists_collection = db['whitelists']

# ... (Baaki saare functions same rahenge jo aapke utils.py me the) ...
# Copy-paste all functions: is_admin, get_config, update_config, etc.
# Bas imports check kar lena.

async def is_admin(client: Client, chat_id: int, user_id: int) -> bool:
    # ... (same logic from utils.py)
    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.user.id == user_id: return True
    return False

# ... (Paste rest of the functions from utils.py here)
