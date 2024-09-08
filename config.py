import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24266722"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5dd6bedd030fd733bb5997a1d62a9b2a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://arafat6six:oyPh2oacHe8OXRwJ@cluster0.sx4en.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
