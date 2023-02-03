#!/usr/bin/python3
""" Librarian Table """

from common.base import Base, myql_session
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from flask import session

class Librarian(Base):
    __tablename__ = 'librarian'
    librarian_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    secret_key = Column(String(1200), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, name="Charles Mbithi", email="charlse@gmail.com", secret_key="1234"):
        self.name = name
        self.email = email
        self.secret_key = secret_key

    def __repr__(self):
        return f"Name {self.name} {self.email}"

    def create_librarian(self):
        librarian = Librarian(
            self.name,
            self.email,
            self.secret_key
        )
        myql_session.add(librarian)
        myql_session.commit()
        myql_session.close()

    @staticmethod
    def get_librarian_by_email(email: str) -> dict:
        """
        """
        librarian: dict = myql_session.query(Librarian).filter(Librarian.email==email).first()
        return librarian
        # return {
        #     "librarian_id": librarian.librarian_id,
        #     "full_name": librarian.full_name,
        #     "email": librarian.email,
        #     "created_at": librarian.created_at
        # }
    
    @staticmethod
    def get_id_by_email(email: str) -> int:
        """
        Parameters
        ----------
        email - librarian email address
        ------
        Return
        ------
        librarian_id (int)
        """
        librarian: int = Librarian.get_librarian_by_email(email)
        return librarian['librarian_id']

    @classmethod
    def get_libarians(cls):
        """
        Return a list of libraians
        """
        libraians = myql_session.query(Librarian).all()
        return [librarian for librarian in libraians]

    @staticmethod
    def delete_librarian(librarian_id):
        """
        Delete user by id
        Args:
            user_id - user id to use for deleting
        """
        user = myql_session.query(Librarian).filter(Librarian.librarian_id==librarian_id).first()
        myql_session.delete(user)
        myql_session.commit()            
        myql_session.close()
