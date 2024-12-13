import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "vjsavecontentbot")
