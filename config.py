import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22182189"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0.6voc3fm.mongodb.net/?retryWrites=true&w=majority")
