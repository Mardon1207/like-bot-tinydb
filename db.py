from tinydb import TinyDB
from tinydb.database import Document

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path, indent=4)
