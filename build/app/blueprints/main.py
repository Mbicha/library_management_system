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

filters = {
        "author": "Author",
        "categories": "Category",
        "isbn_no": "ISBN NO",
        "bk_title": "Title",
        "year_published": "Year Published"
    }

@main.route("/")
def home():
    return render_template('index.html', filters=filters)

# @main.route('/results/<string:bks>')
# def search_results(bks):
#     return render_template('search_results.html', books=bks)

@main.route("/book/search/", methods=['GET', 'POST'])
def book_search():
    if request.method == 'GET':
        return redirect(url_for("main.home"))
    else:
        selected = request.form['search-filter']
        search_filter = request.form['filter_value']
        if selected == 'author':
            books = Book.get_books_by_author(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        elif selected == 'categories':
            books = Book.get_books_by_category(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        elif selected == 'isbn_no':
            book = Book.get_book_by_isbn(search_filter)
            return render_template('search_results.html',
                books=book,
                filter_res=filters[selected]
            )
        elif selected == 'bk_title':
            books = Book.get_books_by_title(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        else:
            books = Book.get_books_by_year_published(int(search_filter))
            books = Book.check_if_empty(books)
            return render_template('search_results.html', books=books)

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

@main.route("/user/update/<string:email_address>", methods=['GET', 'PUT'])
def user_update(email_address):
    if request.method == 'GET':
        user = User.get_by_email(email_address)
        if user is not None:
            return render_template('update_user.html', user=user)
    else:
        full_name = request.form['full_name']
        email_address = request.form['email']
        phone = request.form['phone']        
        password = request.form['password']

        update_user = User(full_name, email_address, phone, password)
        update_user.create_user()
        return render_template('index.html')
