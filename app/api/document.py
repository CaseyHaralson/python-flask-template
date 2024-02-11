from bson import ObjectId
from marshmallow import ValidationError
from pymongo import ReturnDocument
from app.models.document import DocumentSchema
import datetime
from flask import Blueprint, request
from app.infrastructure.document_db import document_db

# the blueprint is registered in the app/api/__init__.py file
document = Blueprint("document", __name__, url_prefix="/document")

_COLLECTION = "document"


@document.route("/test")
def test():
    doc = {
        # 'id': '1',
        "title": "My first document",
        "content": "This is the content of my first document",
        # 'created_at': datetime.datetime(2020, 1, 1, 0, 0, 0),
        # 'updated_at': datetime.datetime.now()
    }
    # result = DocumentSchema().dump(doc)
    # result = DocumentSchema(only=('title', 'content')).dump(doc)
    result = DocumentSchema().load(doc)
    return result


@document.get("/")
def get_all():
    docs = document_db[_COLLECTION].find()
    return DocumentSchema(many=True).dump(docs)


@document.get("/<id>")
def get(id):
    doc = document_db[_COLLECTION].find_one({"_id": ObjectId(id)})
    return DocumentSchema().dump(doc)


@document.post("/create")
def create():
    data = request.json
    try:
        doc = DocumentSchema().load(data)
        doc.pop("_id", None)
        doc["created_at"] = datetime.datetime.utcnow()
        doc["updated_at"] = datetime.datetime.utcnow()
        result = document_db[_COLLECTION].insert_one(doc)
        return str(result.inserted_id), 201
    except ValidationError as err:
        return err.messages, 400


@document.put("/<id>")
def update(id):
    data = request.json
    try:
        doc = DocumentSchema().load(data, partial=True)
        doc.pop("_id", None)
        doc["updated_at"] = datetime.datetime.utcnow()
        result = document_db[_COLLECTION].find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": doc}, return_document=ReturnDocument.AFTER
        )
        return DocumentSchema().dump(result), 201
    except ValidationError as err:
        return err.messages, 400
