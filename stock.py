from analyzer import analyze
from pprint import pprint
from mongo import db
from config import config


class Stock:
    collection_name = "stock"
    db_name = config['mongo']['db']

    def __init__(self, sid, name):
        self.id = sid
        self.name = name
        self.data = {}
        self.ratio = {}

    def set_data(self, data):
        self.data = data

    def set_ratio(self, ratio):
        self.ratio = ratio

    def analyze(self):
        self.set_ratio(analyze(self.data))

    def print(self):
        pprint(self.ratio)

    def save(self):
        data = self.__dict__
        data['_id'] = self.id

        db[self.db_name][self.collection_name].save(data)
