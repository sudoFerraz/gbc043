import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://trabalhosbd:trabalhosbd@localhost/trabalhosbd')
Session = sessionmaker()
engine.echo = False
Session.configure(bind=engine)
session = Session()
print session.query(User)
