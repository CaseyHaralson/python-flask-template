import pymongo
from app.infrastructure.document_db.config import url, db

print("Connecting to document database")
document_client = pymongo.MongoClient(url)
document_db = document_client[db]
