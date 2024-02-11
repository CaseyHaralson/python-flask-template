from flask import Blueprint

# the blueprint is registered in the app/api/__init__.py file
hello = Blueprint("hello", __name__, url_prefix="/hello")


@hello.route("/")
def index():
    return "Hello, World!"
