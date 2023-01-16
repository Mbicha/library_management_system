#!/usr/bin/python3

from base import Base
import enum

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer,String
from sqlalchemy import Enum, Integer

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func


class YesNoChoice(enum.Enum):
    YES = 'Yes'
    NO = 'No'

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email_address = Column(String(60), nullable=False)
    phone = Column(String(30), nullable=True)
    is_admin = Column(Enum(YesNoChoice, values_callable=lambda x: [str(return_choice.value) for return_choice in YesNoChoice]), default='No')
    password = Column(String(15), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, full_name, email_address, phone, pass1):
        self.full_name = full_name
        self.email_address = email_address
        self.phone = phone
        self.password = pass1

    def __repr__(self):
        return f"Name {self.full_name}"

class Book(Base):
    __tablename__ = 'book'
    isbn_no = Column(String(60), primary_key=True)
    bk_title = Column(String(200), nullable=False)
    bk_authors = Column(String(1000), nullable=False)
    categories = Column(String(1000), nullable=True)
    thumbanail = Column(String(1000), nullable=True)
    description = Column(String(5000), nullable=True)
    year_published = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self,isbn, bk_title, bk_authors, categories, thumbnail, desc, year_published):
        self.isbn_no = isbn
        self.bk_title = bk_title
        self.bk_authors = bk_authors
        self.categories = categories
        self.thumbanail = thumbnail
        self.description = desc
        self.year_published = year_published

    def __repr__(self):
        return f"{self.bk_title}"

class Librarian(Base):
    __tablename__ = 'librarian'
    librarian_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email_address = Column(String(60), nullable=False)
    secret_key = Column(String(4), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, full_name, email_address, secret_key):
        self.full_name = full_name
        self.email_address = email_address
        self.secret_key = secret_key

    def __repr__(self):
        return f"Name {self.full_name}"

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

class BK_Return(Base):
    __tablename__ = 'bk_return'
    return_id =  Column(Integer, primary_key = True)
    issue_id = Column(Integer, ForeignKey('issued.issued_id'), nullable=False)
    issued = relationship(Issued)
    is_returned = Column(Enum(YesNoChoice, values_callable=lambda x: [str(return_choice.value) for return_choice in YesNoChoice]))
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, issued_id, isreturned):
        self.issue_id = issued_id
        self.is_returned = isreturned

    def __repr__(self):
        return f"Is the book returned {self.is_returned}"
