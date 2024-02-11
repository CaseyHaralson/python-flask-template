# the blueprint is registered in the app/__init__.py file
from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

# register apis here
from app.api.hello import hello
api.register_blueprint(hello)
from app.api.document import document
api.register_blueprint(document)
