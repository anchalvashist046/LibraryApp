from flask import jsonify, request
from sqlalchemy.orm import Session
from .models import Author, Book
from .db import SessionLocal  # Import the session factory


# ---------- Author Operations ----------
def get_all_authors():
    session = SessionLocal()
    try:
        authors = session.query(Author).all()
        return jsonify([{'id': author.id, 'name': author.name} for author in authors])
    finally:
        session.close()  # Ensure session cleanup


def get_author_by_id(author_id):
    session = SessionLocal()
    try:
        author = session.query(Author).filter(Author.id == author_id).first()
        if not author:
            return jsonify({'error': 'Author not found'}), 404
        return jsonify({'id': author.id, 'name': author.name})
    finally:
        session.close()


def create_author():
    data = request.get_json()
    new_author = Author(name=data['name'])

    session = SessionLocal()
    try:
        session.add(new_author)
        session.commit()
        session.refresh(new_author)  # Ensure ID is set
        return jsonify({'message': 'Author created', 'id': new_author.id})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


def update_author(author_id):
    session = SessionLocal()
    try:
        author = session.query(Author).filter(Author.id == author_id).first()
        if not author:
            return jsonify({'error': 'Author not found'}), 404

        data = request.get_json()
        author.name = data['name']
        session.commit()
        return jsonify({'message': 'Author updated'})
    finally:
        session.close()


def delete_author(author_id):
    session = SessionLocal()
    try:
        author = session.query(Author).filter(Author.id == author_id).first()
        if not author:
            return jsonify({'error': 'Author not found'}), 404

        session.delete(author)
        session.commit()
        return jsonify({'message': 'Author deleted'})
    finally:
        session.close()


# ---------- Book Operations ----------
def get_all_books():
    session = SessionLocal()
    try:
        books = session.query(Book).all()
        return jsonify([
            {'id': book.id, 'title': book.title, 'author': book.author.name}
            for book in books
        ])
    finally:
        session.close()


def get_book_by_id(book_id):
    session = SessionLocal()
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author.name})
    finally:
        session.close()


def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author_id=data['author_id'])

    session = SessionLocal()
    try:
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return jsonify({'message': 'Book created', 'id': new_book.id})
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


def update_book(book_id):
    session = SessionLocal()
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        data = request.get_json()
        book.title = data['title']
        book.author_id = data['author_id']
        session.commit()
        return jsonify({'message': 'Book updated'})
    finally:
        session.close()


def delete_book(book_id):
    session = SessionLocal()
    try:
        book = session.query(Book).filter(Book.id == book_id).first()
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        session.delete(book)
        session.commit()
        return jsonify({'message': 'Book deleted'})
    finally:
        session.close()
