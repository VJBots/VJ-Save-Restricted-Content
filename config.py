import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26276229"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "13aa2e24b15711f6a2213bf8cae0dfdd")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://varmaabhishek97:IhsVfeCDv96pIJD5@cluster0.a6eid.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
