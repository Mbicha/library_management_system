#!/usr/bin/python3

"""Module to create all tables"""

from base import Base, engine, session
from model import Librarian, User, Book, Issued, BK_Return

# create database
Base.metadata.create_all(engine)

class DB_Operations:
    """Common Queries"""
    def get_all(self, table):
        """
        Args:
            table - Target Table
        Return:
            list of objects
        Examples:
            get_all(Book),
            get_all(User)
        """
        books = session.query(table).all()
        session.close()
        return books

    def get_filter_by(self, table, column, value):
        """
        Args:
            table - Target table
            column (string) - Column to search from
            value (string) - Value to search
        Examples:
            get_filter_by(Book, 'isbn', '9780002005883'),
            get_filter_by(User, 'email_address', 'example@gmail.com')
        Return
            List of books matching criteria
        """        
        results = session.query(table).filter_by(column == value).all()
        session.close()
        return results

    def delete_entry(self, table, column, value):
        """
        Args:
            table - Target table
            column (string) - Column to search from
            value (string) - Value to search
        
        Return:
            list of objects without deleted edity

        Examples:
            delete_entry(Book, 'isbn_no','9780002005883')
        """        
        book = session.query(table).filter(table.column == value).delete(synchronize_session=False)
        session.commit()
        session.close()

    def create_book(self, isbn, title, authors, categories, thumbnail, description, year_published):
        """
        Args:
            isbn (string): Book unigue identifier
            bk_title (string): Book title
            bk_authors (string): Author(s) of the book
            categories (string): Book category
            thumbnail (string): Book image url string
            description (string): Short description of the book
            publisher_year (int): Year the book was published
        """
        book = Book(isbn, title, authors, categories, thumbnail, description, year_published)
        session.add(book)
        session.commit()

    
    def create_user(self, full_name, email_address, phone, is_admin, pass1, pass2):
        """
        Args:
            full_name (string) - Names of the user
            email_address (string) - Email of the user
            phone (string) - Phone Number of the user
            is_admin (bool) - whether the user is admin or not
            pass1 (string) - Password to be used by the user when they are logging in
            pass2 (string) - Confirm password
        """
        user = User(full_name, email_address, phone, is_admin, pass1, pass2)
        session.add(user)
        session.commit()
        session.close()
    
    def create_librarian(self, full_name, email_address, secret_key):
        """
        Args:
            full_name (string) - Name of the lobrarian
            email_address (string) - Email address of the librarian
            secret_key (string) - secret key to deferentiate librarian with other users
        Return:
            Librarian object
        """
        librarian = Librarian(full_name, email_address, secret_key)
        session.add(librarian)
        session.commit()
        session.close()

    def create_issued(self, book, librarian, borrower):
        """
        Args:
            book (string) - ISBN of the book being issued
            librarian (int) - Id of the current Librarian
            borrower (int) - Id of the user
        Return:
            Object borrowed
        """
        issued = Issued(book, librarian, borrower)
        session.add(issued)
        session.commit()
        session.close()
