import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8180553726:AAEak58sGN3sRLI1cQtfdWEksBCM8kpgEnI")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25720995"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a6d19ed2823a5790f3e4dcdb6a51c7a4")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1091796386"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vijay112ganesh:yBOdMBRzBF1vvTMB@cluster0.yrfzl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vija112ganesh")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
