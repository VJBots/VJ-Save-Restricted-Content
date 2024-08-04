import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27043578"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "be06bb8e73532042d947bac9d6ee34c0")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://krishnasoni63888:P94txJtapNrxFNRz@cluster0.enblfk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
