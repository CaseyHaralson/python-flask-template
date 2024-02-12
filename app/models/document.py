from app.util.uuid import uuid4_str
from marshmallow import Schema, fields, validate


class DocumentSchema(Schema):
    id = fields.Str(attribute="_id", dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    authors = fields.List(fields.Str(), validate=validate.Length(min=1), required=True)
    figures = fields.List(fields.Nested("FigureSchema"), required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


# https://marshmallow.readthedocs.io/en/stable/nesting.html
class FigureSchema(Schema):
    id = fields.Str(load_default=uuid4_str)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    url = fields.Str(required=True)
