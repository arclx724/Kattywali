# config.py
import os
import re

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

# MongoDB URI
MONGO_URI = "YOUR_MONGODB_URI"

# Default Settings
DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" 
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*'
)
