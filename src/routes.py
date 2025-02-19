from flask import Blueprint
from .controllers import (
    get_all_authors, get_author_by_id, create_author, update_author, delete_author,
    get_all_books, get_book_by_id, create_book, update_book, delete_book
)

api = Blueprint('api', __name__)

# ---------- Author Routes ----------
api.add_url_rule('/authors', 'get_all_authors', get_all_authors, methods=['GET'])
api.add_url_rule('/authors/<int:author_id>', 'get_author_by_id', get_author_by_id, methods=['GET'])
api.add_url_rule('/authors', 'create_author', create_author, methods=['POST'])
api.add_url_rule('/authors/<int:author_id>', 'update_author', update_author, methods=['PUT'])
api.add_url_rule('/authors/<int:author_id>', 'delete_author', delete_author, methods=['DELETE'])

# ---------- Book Routes ----------
api.add_url_rule('/books', 'get_all_books', get_all_books, methods=['GET'])
api.add_url_rule('/books/<int:book_id>', 'get_book_by_id', get_book_by_id, methods=['GET'])
api.add_url_rule('/books', 'create_book', create_book, methods=['POST'])
api.add_url_rule('/books/<int:book_id>', 'update_book', update_book, methods=['PUT'])
api.add_url_rule('/books/<int:book_id>', 'delete_book', delete_book, methods=['DELETE'])

# Register Blueprint
def register_routes(app):
    app.register_blueprint(api)
