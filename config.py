import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7978345492:AAHCn_FeHiEkSEPT1tNxtbor_YwLVqKmQ_A")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22803742"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a35d03d8cbc717e4241202e6dd2b1998")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1558393269"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://bhanwargurjar901:hjyiZDa34iBL1fLm@cluster0.yinab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
