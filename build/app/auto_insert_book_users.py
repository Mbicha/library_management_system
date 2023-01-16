#!/usr/bin/env python3

from db_operations import BookOP, UserOP
from utils.books_to_list import csv_to_list
from utils.generate_users import generate_users

book_op = BookOP()

books_path = "build/data/books.csv"

def add_books(path):
    """
    Args:
        path (csv) - Path for csv file
    Return:
        void
    """
    books_lst = csv_to_list(path)
    for bk in books_lst:
        try:
            book_op.create_book(bk[0], bk[1], bk[2], bk[3], bk[4], bk[5], bk[6])
        except:
            print(f"Error!")

def add_users(num):
    """ 
        Adds automatically generated users to database
        Args:
            num (int) - number of users to be added in the database
        Return:
            void
    """
    userOP = UserOP()
    users = generate_users(num)
    for user in users:
        try:
            userOP.create_user(user[0], user[1], user[2], user[3])
        except:
            print(f"Error!")

if __name__ == "__main__":
    add_books(books_path) # Replace Path with your own
    add_users(100) # Replace 100 with number of users you want
