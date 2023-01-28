#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, abort, url_for, redirect
from models.user import User

user_blueprint  = Blueprint('user_blueprint', __name__)

# User
@user_blueprint.route("/user/new", methods=['GET', 'POST'])
def new_user():
    has_account = False
    if request.method == 'GET':
        return render_template('account.html', has_account=False)
    else:
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']        
        password = request.form['password']
        confrim_password = request.form['confirm_password']

        if password == confrim_password:
            new_user = User(full_name, email, phone, password)
            new_user.create_user()        
            return redirect(url_for('main.books'))
        else:
            return "Passwords are not the sane"

@user_blueprint.route("/user/update/<int:user_id>", methods=['GET', 'POST'])
def user_update(user_id):
    if request.method == 'GET':
        user = User.get_by_id(user_id)
        if user is not None:
            return render_template(
                'account.html',
                user=user,
                has_account=True,
                user_id=user_id
            )
    else:
        full_name = request.form['full_name']
        email_address = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        update_user = User(full_name, email_address, phone, password)
        update_user.create_user()
        return render_template('login.html')
