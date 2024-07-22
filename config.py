import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "16961576"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "029876f95908c0a079023fb116485343")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://gamerboss2452:mMLggPNg51GddaCH@cluster012.vhunxxs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster012")
