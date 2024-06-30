import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22569879"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a193cad6eba083a1cbd4ecf909578159")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://jimmiboy89:jimmiboy89@cluster0.ttsyano.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
