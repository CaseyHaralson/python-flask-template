from marshmallow import Schema, fields, validate


class DocumentSchema(Schema):
    _id = fields.Str()
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
