import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

os.environ['SECRET_KEY'] = 'your_secret_key' # Replace with a strong key
os.environ['DATABASE_URL'] = 'sqlite:///library.db'