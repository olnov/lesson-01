from pymongo import MongoClient

class database(object):
    URI = "mongodb://localhost:27017"
    db = None

    @staticmethod
    def initialize():
        client=MongoClient(database.URI)
        database.db=client['products']

