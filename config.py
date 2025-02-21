import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = "postgresql://postgres:anchal@db:5432/Library_app"
print(f"Connecting to: {DATABASE_URL}")  # for debug

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False