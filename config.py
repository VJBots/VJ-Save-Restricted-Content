import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20237957"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "966fd23c18752262eba14b80324f49c8")

#Database 
DB_URI = os.environ.get("DB_URI", "http://Monster@monster.ztbz76l.mongodb.net/?retryWrites=true&w=majority&appName=Monster")
