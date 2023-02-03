#!/usr/bin/python3

from . book import Book
from . librarian import Librarian
from . user import User
from common.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer,String
from sqlalchemy import Enum, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from common.base import myql_session

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

    def __init__(self, book_isbn, librarian_id, borrower_id):
        self.book_isbn = book_isbn
        self.librarian_id = librarian_id
        self.borrower_id = borrower_id

    def __repr__(self):
        return f"Borrowed {self.book_isbn}"

    def create_issued(self):
        issued = Issued(self.book_isbn, self.librarian_id, self.borrower_id)
        myql_session.add(issued)
        myql_session.commit()
        myql_session.close()
    
    @classmethod
    def get_books_borrowed(cls):
        """
            List of borrowed books
        """
        books_borrowed = myql_session.query(Issued, Book, Librarian, User).join(
                Book, Issued.book_isbn == Book.isbn_no
            ).join(
                Librarian, Issued.librarian_id == Librarian.librarian_id
            ).join(
                User, Issued.borrower_id == User.user_id
            ).all()
        return [book for book in books_borrowed]
