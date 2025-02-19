import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = "postgresql://postgres:anchal@localhost:5432/Library_app"  # Replace your_password

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False