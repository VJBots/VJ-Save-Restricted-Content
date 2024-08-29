import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21911525"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cbf00ad2d16876510d348e2dfcf1352b")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Cluster0:2woaDF8zHlWYnPTD@cluster0.jagjy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
