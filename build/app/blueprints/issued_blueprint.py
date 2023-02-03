#!/usr/bin/env python3

from flask import (Blueprint, render_template, request, session,
                abort, url_for, redirect)
from models.issued import Issued

issued_blueprint  = Blueprint('issued_blueprint', __name__)

@issued_blueprint.route('/issued')
def books_issued():
    issued = Issued.get_books_borrowed()
    return render_template('borrowed.html', issued=issued)
