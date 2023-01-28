#!/usr/bin/env python3

from flask import Blueprint, render_template, request, session, abort, url_for, redirect
from models.user import User

user_blueprint = Blueprint('user_blueprint', __qualname__)

# User
@user_blueprint.route("/user/new", methods=['GET', 'POST'])
def new_user():
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
            return redirect(url_for('main.books'))

@user_blueprint.route("/user/update/<string:email_address>", methods=['GET', 'PUT'])
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
