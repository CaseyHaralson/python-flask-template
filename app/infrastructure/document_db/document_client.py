import os
import pymongo

_user = os.environ.get("MONGO_USER", "mongo")
_pass = os.environ.get("MONGO_PASS", "mongo")
_host = os.environ.get("MONGO_HOST", "localhost")
_port = int(os.environ.get("MONGO_PORT", 27017))
_url = f"mongodb://{_user}:{_pass}@{_host}:{_port}/"

document_client = pymongo.MongoClient(_url)
