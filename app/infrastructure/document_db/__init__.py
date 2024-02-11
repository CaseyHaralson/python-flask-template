import pymongo
from app.infrastructure.document_db.config import url

document_client = pymongo.MongoClient(url)
