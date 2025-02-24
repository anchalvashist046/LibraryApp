from flask import Blueprint
from .controllers import create_library_item, get_library_items, update_library_item, delete_library_item

api = Blueprint('api', __name__)

api.add_url_rule('/library', 'create_library_item', create_library_item, methods=['POST'])
api.add_url_rule('/library', 'get_library_items', get_library_items, methods=['GET'])
api.add_url_rule('/library/author/<int:item_id>', 'update_author', lambda item_id: update_library_item(item_id, 'author'), methods=['PUT'])
api.add_url_rule('/library/book/<int:item_id>', 'update_book', lambda item_id: update_library_item(item_id, 'book'), methods=['PUT'])
api.add_url_rule('/library/author/<int:item_id>', 'delete_author', lambda item_id: delete_library_item(item_id, 'author'), methods=['DELETE'])
api.add_url_rule('/library/book/<int:item_id>', 'delete_book', lambda item_id: delete_library_item(item_id, 'book'), methods=['DELETE'])

def register_routes(app):
    app.register_blueprint(api)