from bson import ObjectId
from marshmallow import ValidationError
from pymongo import ReturnDocument
from app.models.document import DocumentSchema, FigureSchema
import datetime
from flask import Blueprint, request
from app.infrastructure.document_db import document_db

# the blueprint is registered in the app/api/__init__.py file
document = Blueprint("document", __name__, url_prefix="/document")

_COLLECTION = "document"


@document.get("/")
def get_all():
    docs = document_db[_COLLECTION].find()
    return DocumentSchema(many=True).dump(docs)


@document.get("/<id>")
def get(id):
    doc = document_db[_COLLECTION].find_one({"_id": ObjectId(id)})
    if doc is None:
        return {"message": "Document not found"}, 404
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
        created_doc = document_db[_COLLECTION].find_one({"_id": result.inserted_id})
        return DocumentSchema().dump(created_doc), 201
    except ValidationError as err:
        return err.messages, 400


@document.put("/<id>")
def update(id):
    data = request.json
    try:
        # using partial=True allows for partial creation of sub-schemas (it worked great til a sub-schema was added to the DocumentSchema)
        # this means that required fields on the sub-schema are not required when adding new figures...
        # so we use partial=("title", "content", "authors", "figures") to specify what can be partial
        # and figures is now not required, but if it is provided, the figures schema will be fully required...
        # a new endpoint will need to be added to handle partial updates of sub-schemas...
        # doc = DocumentSchema().load(data, partial=True)
        doc = DocumentSchema().load(
            data, partial=("title", "content", "authors", "figures")
        )
        doc.pop("_id", None)
        doc["updated_at"] = datetime.datetime.utcnow()
        result = document_db[_COLLECTION].find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": doc}, return_document=ReturnDocument.AFTER
        )
        if result is None:
            return {"message": "Document not found"}, 404
        return DocumentSchema().dump(result), 200
    except ValidationError as err:
        return err.messages, 400


# this doesn't allow for partial edits of a figure
# but it does allow for a particular figure from the document to be updated...
@document.put("/<id>/figure")
def update_figure(id):
    data = request.json
    try:
        figure = FigureSchema().load(data)
        figure_id = figure["id"]
        updated_at = datetime.datetime.utcnow()
        result = document_db[_COLLECTION].find_one_and_update(
            {"_id": ObjectId(id), "figures.id": figure_id},
            {"$set": {"updated_at": updated_at, "figures.$": figure}},
            return_document=ReturnDocument.AFTER,
        )
        if result is None:
            return {"message": "Document or figure not found"}, 404
        return DocumentSchema().dump(result), 200
    except ValidationError as err:
        return err.messages, 400


@document.delete("/<id>")
def delete(id):
    result = document_db[_COLLECTION].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return {"message": "Document not found"}, 404
    return "", 204
