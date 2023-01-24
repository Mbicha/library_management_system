#!/usr/bin/env python3

import os
from flask import Blueprint, render_template, request, session, abort, url_for, redirect
from models.user import User
from models.book import Book


# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# TEMPLATES_DIR = os.path.join(template_dir, 'build/frontend/templates')
# STATIC_DIR = os.path.join(template_dir, 'build/frontend/static')

# print(TEMPLATES_DIR)
# , template_folder="../../frontend/templates/", static_folder="../../frontend/static/

main = Blueprint('main',__name__)

has_account = False

@main.route("/")
def home():
    return render_template('index.html')


@main.route("/books/new", methods=['GET', 'POST', 'PUT'], strict_slashes=False)
def new_book():
    if request.method == 'GET':
        return render_template('edit_book.html')
    else:
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        thumbnail = request.form['thumbnail']
        description = request.form['description']
        year_published = request.form['year_published']

        book = Book(isbn, title, author, category, thumbnail, description, year_published)
        book.create_book()
        return redirect(url_for('main.books'))

@main.route("/books", strict_slashes=False)
def books():
    books = Book.get_books()
    return render_template('books_list.html', books=books)

@main.route("/book_details/<string:isbn_no>", strict_slashes=False)
def book_details(isbn_no):
    book = Book.get_book_by_isbn(isbn_no)
    return render_template('book_details.html', book=book)

@main.route("/borrowed/")
def borrowed():
    return render_template('borrowed.html')

# User
@main.route("/user/new", methods=['GET', 'POST'])
def new_new():
    if request.method == 'GET':
        return render_template('account.html')
    else:
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']        
        password = request.form['password']
        confrim_password = request.form['confirm_password']

        if password == confrim_password:
            new_user = User(full_name, email, phone, password)
            new_user.create_user()        
            return render_template('index.html')

@main.route("/user/update/<string:email_address>", methods=['GET', 'PUT', 'DELETE'])
def user_update(email_address):
    if request.method == 'GET':
        return render_template('update_user.html', user=User.get_by_email(email_address))
    elif request.method == 'PUT':
        full_name = request.form['full_name']
        email_address = request.form['email']
        phone = request.form['phone']        
        password = request.form['password']

        User.update_user(full_name, email_address, phone, password)
        return render_template('index.html')

# @main.route("/admin/login", methods=['GET','POST'])
# def login_user():
#     if request.method == 'GET':
#         return render_template('admin_login.html')

#     else:
#         email = request.form['email']
#         password = request.form['password']

#         if Admin.is_admin_logins_valid(email, password):
#             Admin.login(email)
#         else:
#             session['email_address'] =  None

#         return render_template('index.html', email_address=session['email_address'])
