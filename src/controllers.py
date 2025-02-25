from flask import jsonify, request
from sqlalchemy.orm import Session
from .models import Author, Book
from .db import SessionLocal  # Import the session factory
from datetime import datetime  # Add this lin

# ---------- Author Operations ----------

# new api end point
def create_library_item():
    session = SessionLocal()
    try:
        data = request.get_json()
        author_data = data.get('author')
        book_data = data.get('book')

        if not author_data or not book_data:
            return jsonify({'error': 'Author and Book data are required'}), 400

        author = None
        author_id = author_data.get('id')
        author_name = author_data.get('name')

        if author_id:
            author = session.query(Author).filter_by(id=author_id).first() #why
        elif author_name:
            author = session.query(Author).filter_by(name=author_name).first()

        if not author:
            author = Author(
                name=author_data['name'],
                bio=author_data.get('bio'),
                nationality=author_data.get('nationality')
            )
            session.add(author)
            session.flush()  # flush to get the new author.id

        existing_book = session.query(Book).filter_by(title=book_data['title'], author_id=author.id).first()

        if existing_book:
            return jsonify({'message': 'Book already exists for this author'}), 409

        book = Book(
            title=book_data['title'],
            genre=book_data.get('genre'),
            author_id=author.id,
            published_date=datetime.strptime(book_data['published_date'], '%Y-%m-%d').date() if book_data.get('published_date') else None,
            lang=book_data.get('lang'),
            price=book_data.get('price'),
            availability=book_data.get('availability', True)
        )
        session.add(book)

        session.commit()
        return jsonify({'message': 'Book added to author successfully'}), 201

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()

# create a Get API
def get_library_items():
    session = SessionLocal()
    try:
        # Get query parameters
        author_id = request.args.get('author_id', type=int)
        author_name = request.args.get('author_name')
        book_id = request.args.get('book_id', type=int)
        book_title = request.args.get('book_title')

        query = session.query(Author)

        # Apply filters based on query parameters
        if author_id:
            query = query.filter(Author.id == author_id)
        if author_name:
            query = query.filter(Author.name.ilike(f"%{author_name}%"))  # Case-insensitive like search
        if book_id:
            query = query.join(Author.books).filter(Book.id == book_id)
        if book_title:
            query = query.join(Author.books).filter(Book.title.ilike(f"%{book_title}%"))

        authors = query.all()

        result = []
        for author in authors:
            author_data = {
                'id': author.id,
                'name': author.name,
                'bio': author.bio,
                'nationality': author.nationality,
                'created_at': author.created_at.isoformat(),
                'books': [
                    {
                        'id': book.id,
                        'title': book.title,
                        'genre': book.genre,
                        'published_date': book.published_date.isoformat() if book.published_date else None,
                        'lang': book.lang,
                        'price': book.price,
                        'availability': book.availability,
                        'created_at': book.created_at.isoformat(),
                    }
                    for book in author.books
                ],
            }
            result.append(author_data)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

# api for update
def update_library_item():
    session = SessionLocal()
    try:
        author_id = request.args.get('author_id', type=int)
        book_id = request.args.get('book_id', type=int)
        data = request.get_json()

        if author_id:
            author = session.query(Author).filter_by(id=author_id).first()
            if not author:
                return jsonify({'error': 'Author not found'}), 404
            for key, value in data.items():
                if hasattr(author, key):
                    setattr(author, key, value)
        elif book_id:
            book = session.query(Book).filter_by(id=book_id).first()
            if not book:
                return jsonify({'error': 'Book not found'}), 404
            for key, value in data.items():
                if hasattr(book, key):
                    if key == 'published_date' and value:
                        setattr(book, key, datetime.strptime(value, '%Y-%m-%d').date())
                    else:
                        setattr(book, key, value)
        else:
            return jsonify({'error': 'Author ID or Book ID is required'}), 400

        session.commit()
        return jsonify({'message': 'Library item updated successfully'}), 200

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

# API for delete
# def delete_library_item():
#     session = SessionLocal()
#     try:
#         author_id = request.args.get('author_id', type=int)
#         book_id = request.args.get('book_id', type=int)
#         delete_author_with_books = request.args.get('delete_author_with_books', type=bool, default=False)
#
#         if author_id:
#             author = session.query(Author).filter_by(id=author_id).first()
#             if not author:
#                 return jsonify({'error': 'Author not found'}), 404
#
#             if delete_author_with_books:
#                 # Delete author and all associated books
#                 for book in author.books:
#                     session.delete(book)
#                 session.delete(author)
#                 session.commit()
#                 return jsonify({'message': 'Author and associated books deleted successfully'}), 200
#
#             else:
#                 # Delete author only if they have no books
#                 if not author.books:
#                     session.delete(author)
#                     session.commit()
#                     return jsonify({'message': 'Author deleted successfully'}), 200
#                 else:
#                     return jsonify({'error': 'Author has associated books. Use delete_author_with_books=True to delete'}), 400
#
#         elif book_id:
#             book = session.query(Book).filter_by(id=book_id).first()
#             if not book:
#                 return jsonify({'error': 'Book not found'}), 404
#
#             author_id = book.author_id  # Save author_id before deleting the book
#
#             session.delete(book)
#             session.commit()
#
#             # Check if the author has any remaining books
#             author = session.query(Author).filter_by(id=author_id).first()
#             if author and not author.books:
#                 session.delete(author)
#                 session.commit()
#                 return jsonify({'message': 'Book and author deleted successfully'}), 200
#             else:
#                 return jsonify({'message': 'Book deleted successfully'}), 200
#
#         else:
#             return jsonify({'error': 'Author ID or Book ID is required'}), 400
#
#     except Exception as e:
#         session.rollback()
#         return jsonify({'error': str(e)}), 500
#     finally:
#         session.close()