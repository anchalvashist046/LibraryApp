

from flask import Flask
from library_application import create_app  # Import the create_app function

app = create_app()  # Create the Flask app instance


@app.route("/")
def home():
    return "Welcome to the Library App"

if __name__ == "__main__":
    app.run(debug=True)

