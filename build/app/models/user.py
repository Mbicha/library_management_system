#!/usr/bin/python3
""" User Table """

from common.base import Base, myql_session
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from flask import session

class User(Base, object):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email_address = Column(String(60), nullable=False)
    phone = Column(String(30), nullable=True)
    password = Column(String(15), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, full_name, email_address, phone, password):
        self.full_name = full_name
        self.email_address = email_address
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"Name {self.full_name}"

    def create_user(self):
        """
        Args:
            full_name (string) - Names of the user
            email_address (string) - Email of the user
            phone (string) - Phone Number of the user
            is_admin (bool) - whether the user is admin or not
            pass1 (string) - Password to be used by the user when they are logging in
            pass2 (string) - Confirm password
        """
        user = User.get_by_email(self.email_address)
        if user is None:
            new_user = User(self.full_name, self.email_address, self.phone, self.password)
            myql_session.add(new_user)
            myql_session.commit()
            myql_session.close()
        else:
            self.update_user()

    @classmethod
    def update_user(cls, full_name, email_address, phone, password):
        """
        Updates User
        """
        user = User.get_by_email(email_address)
        if user is not None:
            id = User.get_id_by_email(email_address)

            new_user_data = {
                "full_name": full_name,
                "email_address": email_address,
                "phone": phone,
                "password": password
            }

            myql_session.query(User).filter(
                User.user_id == id
            ).update(new_user_data)
            myql_session.commit()
            myql_session.flush()
            myql_session.close()
        else:
            new_user = User(full_name, email_address, phone, password)
            new_user.create_user()

    def delete_user(cls, user_id):
        """
        Delete user by id
        Args:
            user_id - user id to use for deleting
        """
        myql_session.query(User).filter(User.user_id == user_id).delete(synchronize_session=False)
        User.logout()
        myql_session.commit()
        myql_session.close()
    
    @classmethod
    def get_by_email(cls, email_address):
        """
        Args:
            email_address - get user object
        Return:
            User object
        """
        user = myql_session.query(User).filter(
            User.email_address==email_address).first()
        if user is not None:
            return {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "email_address": user.email_address,
                "phone": user.phone,
                "password": user.password
            }

    @classmethod
    def get_id_by_email(cls, email_address):
        user_id = User.get_by_email(email_address)['user_id']
        if user_id is not None:
            return user_id
        else:
            return False

    @classmethod
    def is_logins_valid(cls, email_address, password):
        user = User.get_by_email(email_address)
        if user is not None:
            return user.password == password
        else:
            return False
    
    @staticmethod
    def login(email_address):
        session['email_address'] = email_address
    
    @staticmethod
    def logout():
        session['email_address'] = None

# user = User("Mbithi Rhoda", "mbithicharlse@gmail.com", "98573123", "1234")

# print("Get User By Email\n\n")
# print(user.get_by_email("mbithicharlse@gmail.com"))
# print("Get ID By Email\n")
# print(user.get_id_by_email("mbithicharlse@gmail.com"))
# user.update_user()
# print("Updated\n\n")
# print(user.get_by_email("mbithicharlse@gmail.com"))
# try:
#     user.delete_user(55)
#     print(f"success")
# except:
#     print(f"Error deleting user")