from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///newtutorial.db', echo=True)
Base = declarative_base()

class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    fname = Column(String)
    lname = Column(String)

    def __init__(self, username, password, fname, lname):
        """"""
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname

class Contact(Base):
    """"""
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    local_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    address = Column(String)
    contact = Column(String)

    local = relationship('User', foreign_keys=local_id)

    def __init__(self, name, address, contact):
        """"""
        self.name = name
        self.address = address
        self.contact = contact

# create tables
Base.metadata.create_all(engine)
