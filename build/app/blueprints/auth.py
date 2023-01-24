# #!/usr/bin/env python3

# from flask import Blueprint, request, redirect, render_template, url_for, abort
# from db_operations import DB_Operations
# from model import Book, Librarian, User, Issued, BK_Return

# auth = Blueprint('auth', __name__)

# @auth.route('/login/', methods=['POST'])
# def login():
#     return render_template('login.html')

# @auth.route('/account')
# def account():
#     return render_template('account.html')

# @auth.route("/account/", methods=['GET', 'POST'], strict_slashes=False)
# def post_account():
#     user = DB_Operations()
#     if request.method == 'POST':
#         name = request.form['full_name']
#         email = request.form['email']
#         phone = request.form['phone']
#         admin = request.form['is_admin']
#         pass1 = request.form['password']
#         pass2 = request.form['confirm_password']
#         if pass1 == pass2:
#             try:
#                 user.create_user(name, email, phone, admin, pass1, pass2)
#                 return redirect(url_for('auth.login'))
#             except:
#                 abort(404)

# @auth.route('/logout')
# def logout():
#     return 'Logout'
