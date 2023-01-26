#!/usr/bin/python3
""" Librarian Table """

from models.librarian import Librarian
from common.base import Base, myql_session
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

class Librarian(Base):
    __tablename__ = 'librarian'
    librarian_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email_address = Column(String(60), nullable=False)
    secret_key = Column(String(4), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, full_name, email_address, secret_key):
        self.full_name = full_name
        self.email_address = email_address
        self.secret_key = secret_key

    def __repr__(self):
        return f"Name {self.full_name}"

    def create_librarian(self):
        librarian = Librarian(
            self.full_name,
            self.email_address,
            self.secret_key
        )
        myql_session.add(librarian)
        myql_session.commit()
        myql_session.close()
