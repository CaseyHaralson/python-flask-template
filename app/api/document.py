# the blueprint is registered in the app/api/__init__.py file
from flask import Blueprint
document = Blueprint('document', __name__, url_prefix='/document')

from app.infrastructure.document_db import document_client
db = document_client['db']

@document.route('/create')
def create():
    collection = db['document']
    return 'Hello, World!'
