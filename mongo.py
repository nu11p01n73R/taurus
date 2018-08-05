from pymongo import MongoClient
from config import config


db = MongoClient(config['mongo']['url'])
