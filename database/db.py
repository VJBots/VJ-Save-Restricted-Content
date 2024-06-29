from pymongo import MongoClient
from config import DB_URI

mongo_client = MongoClient(DB_URI)
database = mongo_client.userdb.sessions
