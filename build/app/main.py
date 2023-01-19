#!/usr/bin/env python3

import os
from db_operations import DB_Operations, BookOP
from flask import Blueprint, render_template, request, abort, url_for, redirect
from model import Book
from utils.books_to_list import csv_to_list


# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# TEMPLATES_DIR = os.path.join(template_dir, 'build/frontend/templates')
# STATIC_DIR = os.path.join(template_dir, 'build/frontend/static')

# print(TEMPLATES_DIR)
# , template_folder="../../frontend/templates/", static_folder="../../frontend/static/

main = Blueprint('main',__name__)


@main.route("/")
def home():
    return render_template('index.html')


@main.route("/create_book/", methods=['GET', 'POST'], strict_slashes=False)
def create_book():
    bk = DB_Operations()
    if request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        thumbnail = request.form['thumbnail']
        description = request.form['description']
        year_published = request.form['year_published']

        try:
            bk.create_book(isbn, title, author, category, thumbnail, description, year_published)
            return redirect(url_for('books_list'))
        except:
            abort(404)
    return render_template('edit_book.html')

@main.route("/books_list/")
def books_list():
    bk = DB_Operations()
    books = bk.get_all(Book)
    return render_template('books_list.html', books=books)

# @main.route("/book_details")
# def book_details():
#     return render_template('book_details.html')

@main.route("/book_details/<string:isbn_no>", methods=['GET'])
def get_details(isbn_no):
    bk = BookOP()
    single_bk = bk.get_book_by_isbn(isbn_no)
    return render_template('book_details.html', book=single_bk)

@main.route("/borrowed/")
def borrowed():
    return render_template('borrowed.html')
