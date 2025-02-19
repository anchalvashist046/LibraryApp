import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = os.environ.get('DATABASE_URL') or \
    "postgresql://library_user:anchal@localhost:5432/Library_app"  # Replace your_password

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False