from flask import jsonify, request
from .models import Author, Book
from . import db

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
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'message': 'Author created', 'id': new_author.id})

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
    db.session.add(new_book)
    db.session.commit()
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