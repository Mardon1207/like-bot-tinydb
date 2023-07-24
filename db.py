from tinydb import TinyDB,Query
from tinydb.database import Document
import os 

TOKEN = os.environ['TOKEN']
class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path, indent=4)
    def save(self,chat_id):
        user=Document({
            "like":0,
            "dislike":0
        },doc_id=chat_id)
        self.db.insert(user)
    def like(self,chat_id):
        like=self.db.get(doc_id=chat_id)["like"]
        user={"like":like+1}
        self.db.update(user, doc_ids=[chat_id])
    def dislike(self,chat_id):
        dislike=self.db.get(doc_id=chat_id)["dislike"]
        user={"dislike":dislike+1}
        self.db.update(user,doc_ids=[chat_id])
    def add_like(self,chat_id):
        like=self.db.get(doc_id=chat_id)["like"]
        return like
    def add_dislike(self,chat_id):
        dislike=self.db.get(doc_id=chat_id)["dislike"]
        return dislike