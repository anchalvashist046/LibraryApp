from flask import Flask
import os
from .db import engine, get_db, Base  # Import engine, get_db, and Base

def create_app(config_filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.py")):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    # Initialize db and create tables within the application context
    with app.app_context():
        Base.metadata.create_all(engine)  # Create tables

    from .routes import register_routes
    register_routes(app)

    return app

app = create_app()