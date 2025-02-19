# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime  # Import datetime here
#
# db = SQLAlchemy()  # Initialize SQLAlchemy globally
#
# def create_app(config_filename="config.py"): # allows for different configs
#     app = Flask(__name__)
#     app.config.from_pyfile(config_filename) # load the config file
#
#     db.init_app(app)  # Initialize database with the app
#     with app.app_context(): # Create app context for db initialization
#         db.create_all()  # Create database tables if they don't exist
#
#     from .routes import register_routes # Import routes
#     register_routes(app) # register routes
#
#     return app

from flask import Flask

def create_app(config_filename="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    # If you have models defined using SQLAlchemy's Base, you can import them and create tables:
    from db import engine  # your raw SQLAlchemy engine
    from models import Base  # assuming you use declarative_base() in your models

    # Create tables (you might want to do this conditionally)
    Base.metadata.create_all(engine)

    from .routes import register_routes  # Import routes
    register_routes(app)  # register routes

    return app
