import os

from pymongo import MongoClient


class BaseDao:
    """Singleton Base Database Object for MongoDB
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Creates the DB client
            client = MongoClient(os.getenv("MONGO_URL"))
            # Sets collection to "reversi"
            cls.db = client.reversi
        return cls._instance
