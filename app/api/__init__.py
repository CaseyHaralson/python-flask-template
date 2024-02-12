from flask import Blueprint
from app.api.hello import hello
from app.api.document import document

# the blueprint is registered in the app/__init__.py file
api = Blueprint("api", __name__, url_prefix="/api")

# register apis here
api.register_blueprint(hello)
# .pinkyring=MONGO
api.register_blueprint(document)
# .pinkyring=MONGO.end
