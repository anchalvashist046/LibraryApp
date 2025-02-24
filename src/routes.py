from flask import Blueprint
from .controllers import create_library_item,get_library_items

api = Blueprint('api', __name__)

# ---------- Library Routes ----------
api.add_url_rule('/library', 'create_library_item', create_library_item, methods=['POST'])
api.add_url_rule('/library', 'get_library_item', get_library_items, methods=['GET'])


# Register Blueprint
def register_routes(app):
    app.register_blueprint(api)
