#!/usr/bin/python3

from book import Book
from librarian import Librarian
from user import User
from common.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer,String
from sqlalchemy import Enum, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

class Issued(Base):
    __tablename__ = 'issued'
    issued_id = Column(Integer, primary_key=True)
    issued_date = Column(DateTime(timezone=True), default=func.now())
    book_isbn = Column(String(60), ForeignKey('book.isbn_no'), nullable=False)
    librarian_id = Column(Integer, ForeignKey('librarian.librarian_id'), nullable=False)
    borrower_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    book = relationship(Book)
    librarian = relationship(Librarian)
    borrower = relationship(User)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, book, librarian, borrower):
        self.book_isbn = book
        self.librarian_id = librarian
        self.borrower_id = borrower

    def __repr__(self):
        return f"Borrowed {self.book_isbn}"
