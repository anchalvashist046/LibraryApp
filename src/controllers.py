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

        author = None # why?

        if author_data:
            author = Author(
                name=author_data['name'],
                bio=author_data.get('bio'),
                nationality=author_data.get('nationality')
            )
            session.add(author)
            session.flush() #why

        if book_data:
          book = Book(
              title=book_data['title'],
              genre=book_data.get('genre'),
              author_id=author.id if author_data else book_data['author_id'],
              published_date=datetime.strptime(book_data['published_date'], '%Y-%m-%d').date() if book_data.get(
                'published_date') else None,
              lang=book_data.get('lang'),
              price=book_data.get('price'),
              availability=book_data.get('availability', True)
          )
          session.add(book)

        session.commit()
        return jsonify({'message': 'Library item created successfully'}), 201

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        session.close()


# create a Get API
def get_library_items():
    session = SessionLocal()
    try:
        authors = session.query(Author).all()
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
def update_library_item(item_id, item_type):
    session = SessionLocal()
    try:
        data = request.get_json()
        if item_type == 'author':
            item = session.query(Author).filter_by(id=item_id).first()
            if not item:
                return jsonify({'error': 'Author not found'}), 404
            for key, value in data.items():
                if hasattr(item, key):
                    setattr(item, key, value)
        elif item_type == 'book':
            item = session.query(Book).filter_by(id=item_id).first()
            if not item:
                return jsonify({'error': 'Book not found'}), 404
            for key, value in data.items():
                if hasattr(item, key):
                    if key == 'published_date' and value:
                        setattr(item, key, datetime.strptime(value, '%Y-%m-%d').date())
                    else:
                        setattr(item, key, value)

        else:
            return jsonify({'error': 'Invalid item type'}), 400

        session.commit()
        return jsonify({'message': f'{item_type.capitalize()} updated successfully'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

# API for delete
def delete_library_item(item_id, item_type):
    session = SessionLocal()
    try:
        if item_type == 'author':
            item = session.query(Author).filter_by(id=item_id).first()
        elif item_type == 'book':
            item = session.query(Book).filter_by(id=item_id).first()
        else:
            return jsonify({'error': 'Invalid item type'}), 400

        if not item:
            return jsonify({'error': f'{item_type.capitalize()} not found'}), 404

        session.delete(item)
        session.commit()
        return jsonify({'message': f'{item_type.capitalize()} deleted successfully'}), 200
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()



