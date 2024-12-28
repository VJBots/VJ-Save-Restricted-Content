import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7908557119:AAGRUsIVAFKaSodKrGa7Yigj7EOfnuX-oz0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20970729"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "38ea2ec0268abb447f1fb96223c53c22")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1454341062"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://abinetolke80:<db_password>@cluster0.7qpb3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "abinetolke80")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
