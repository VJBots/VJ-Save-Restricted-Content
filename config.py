import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23846467"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5de58cc497de047ba384c104ffea89a5")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://tipendrathebest:lgiSksSyVDsRgn0t@cluster0.zubtivr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
