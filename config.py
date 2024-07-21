import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26928239"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "eb5835a09739eba31d78971be7492d24")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb-srv://tnbots:tnbots@cluster0.Jkures.mongodb.net/?retryWrites=true&w=majority")
