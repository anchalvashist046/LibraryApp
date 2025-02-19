from flask import jsonify, request
from .models import Author, Book
from .db import get_db # Import the get_db function

# ---------- Author Operations ----------
def get_all_authors():
    authors = Author.query.all()
    return jsonify([{'id': author.id, 'name': author.name} for author in authors])

def get_author_by_id(author_id):
    author = Author.query.get_or_404(author_id)
    return jsonify({'id': author.id, 'name': author.name})

def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'])

    db = get_db().__next__()  # Get the database session

    db.add(new_author)
    try:
        db.commit()
        db.refresh(new_author)  # Refresh the new_author object to get the ID
        return jsonify({'message': 'Author created', 'id': new_author.id})
    except Exception as e:
        db.rollback()  # Rollback in case of any error
        return jsonify({'error': str(e)}), 500  # Return error message

def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    data = request.get_json()
    author.name = data['name']
    db.session.commit()
    return jsonify({'message': 'Author updated'})

def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': 'Author deleted'})

# ---------- Book Operations ----------
def get_all_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author.name} for book in books])

def get_book_by_id(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author.name})

def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'])
    db = get_db().__next__()  # Get the db session from the generator

    db.add(new_book)
    db.commit()
    db.refresh(new_book)  # Refresh the new_book object to get the ID
    return jsonify({'message': 'Book created', 'id': new_book.id})

def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data['title']
    book.author_id = data['author_id']
    db.session.commit()
    return jsonify({'message': 'Book updated'})

def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})