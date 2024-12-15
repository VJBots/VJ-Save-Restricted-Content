import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29226750"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e2772ee6aba52f15e72ac9684c38f54c")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://devilkumarali006:dtcsaYfS26Ceh9em@cluster0.ekho2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
