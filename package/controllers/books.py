
def get_book():
    books= Book.query.all() #SQLAlchemy query
    book_list=[]
    for book in books:
        book_data= {
            'id':book.id,
            'title':book.title,
            'author':book.author.name if book.author else None
        }
        book_list.append(book_data)
    return jsonify(book_list),200

def create_book():
    data= request.get_json() #this is a post request which retrieves the content type json
    title=data.get('title')
    author_id= data.get('author_id')

    author = Author.query.get(author_id) #SQLAlchemy query
    if not author:
        return jsonify({'message':'Author not found'}), 404

    new_book= Book(title=title, author_id=author_id)
    db.session.add(new_book) #db is the SQLAlchemy instance created in app
    db.session.commit()

    return jsonify({'message':'Book created sucessfully'}), 201


