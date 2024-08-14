import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27624796"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6b0f47e65d111feca7b0f16f795f2ecb")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://charanabhay108:charanabhay108@cluster0.8oy6x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
