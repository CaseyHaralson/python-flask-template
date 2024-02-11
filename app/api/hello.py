# the blueprint is registered in the app/api/__init__.py file
from flask import Blueprint
hello = Blueprint('hello', __name__, url_prefix='/hello')

@hello.route('/')
def index():
    return 'Hello, World!'
