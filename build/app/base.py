#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from secrets_file import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

# def get_session():
#     Base.metadata.create_all(engine)
#     return _session
