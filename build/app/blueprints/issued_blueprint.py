#!/usr/bin/env python3

from flask import (Blueprint, render_template, request, session,
                abort, url_for, redirect)
from models.issued import Issued
from models.user import User
from models.librarian import Librarian

issued_blueprint  = Blueprint('issued_blueprint', __name__)

@issued_blueprint.route('/issued')
def books_issued():
    issued = Issued.get_books_borrowed()
    return render_template('borrowed.html', issued=issued)

@issued_blueprint.route('/borrowed/more_details/<int:issued_id>')
def more_borrowed_details(issued_id):
    more_details = Issued.get_book_borrowed_by_issued_id(issued_id)
    return render_template('more_details_on_book_borrowed.html', more_details=more_details)
