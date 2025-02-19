from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Date,
    Boolean,
)
from sqlalchemy.orm import relationship, declarative_base

# Create a declarative base
Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    bio = Column(Text)
    nationality = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Define relationship with Book
    books = relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.name}>'


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    genre = Column(String(100))
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    published_date = Column(Date)
    lang = Column(String(50))
    price = Column(Integer)
    availability = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Book {self.title}>'
