

from flask import Flask
from src import create_app

app = create_app()  # Create the Flask app instance


@app.route("/")
def home():
    return "Welcome to the Library App"

if __name__ == "__main__":
    app.run(debug=True)

