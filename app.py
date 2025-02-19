# from app import create_app, db
#
# app = create_app()
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create tables if they don't exist
#     app.run(debug=True)

from flask import Flask
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import config


app = Flask(__name__)
app.config.from_object(Config)

# Database setup
engine = sqlalchemy.create_engine(Config.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)

@app.route("/")
def home():
    return "Welcome to the Library App"

if __name__ == "__main__":
    app.run(debug=True)
