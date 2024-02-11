import os
import pymongo

_user = os.environ.get("MONGO_USER", "mongo")
_pass = os.environ.get("MONGO_PASS", "mongo")
_host = os.environ.get("MONGO_HOST", "localhost")
_port = int(os.environ.get("MONGO_PORT", 27017))
url = f"mongodb://{_user}:{_pass}@{_host}:{_port}/"

db = os.environ.get("MONGO_DB", "db")
