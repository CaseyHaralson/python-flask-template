from flask import Blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/hello')
def hello():
    return 'Hello, World!'
