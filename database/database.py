# database/database.py
from pymongo import MongoClient, ReturnDocument

class Database:
    def __init__(self, uri: str = "mongodb://localhost:27017/", db_name: str = "sistema_tarefas"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name: str):
        return self.db[name]

    def next_id(self, name: str) -> int:
        counter = self.db["counters"].find_one_and_update(
            {"_id": name},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        return int(counter["seq"])
