""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''



### INSPO DATABASE

# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Inspo(db.Model):
    __tablename__ = 'Inspo_data'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    
    # Define the Notes schema
    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _quote = db.Column(db.String, unique=False, nullable=False)
    
    # userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    # userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, quote):
        self.userID = id
        self._uid = uid
        self._quote = quote

    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # workouts = db.relationship("workouts", cascade='all, delete', backref='users', lazy=True)
    # inspo = db.relationship("inspo", cascade='all, delete', backref='users', lazy=True)
    # ISPE = db.relationship("ISPE", cascade='all, delete', backref='users', lazy=True)
    # InputWork = db.relationship("InputWork", cascade='all, delete', backref='users', lazy=True)

     # FOR INSPO PAGE:

    @property
    def uid(self):
        return self._uid
    
    # a setter function, allows name to be updated after initial object creation
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid
     # a getter method, extracts email from object
   # @property
    #def id(self):
     #   return self._id
    
    # a setter function, allows name to be updated after initial object creation
   # @id.setter
    #def id(self, id):
     #   self._id = id
    
    # a getter method, extracts email from object
    @property
    def quote(self):
        return self._quote
    
    # a setter function, allows name to be updated after initial object creation
    @quote.setter
    def quote(self, quote):
        self._quote = quote
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "uid": self.uid,
            # "userID": self.userID,
            "quote": self.quote
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, uid='', quote=""):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(quote) > 0:
            self.quote = quote
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initInspos():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = Inspo(id='2', uid='alexa2', quote= 'You are strong')
        i2 = Inspo(id='11', uid='ava2', quote= 'Do not quit!')
        i3 = Inspo(id='55', uid='lydia2', quote= 'Slay bestie')
        i4 = Inspo(id='33', uid='Sri2', quote= 'be like super mort')
        i5 = Inspo(id='44', uid='Nikhil2', quote= 'hard work beats talent!')

        inspos = [i1, i2, i3, i4, i5]

        """Builds sample user/note(s) data"""
        for inspo in inspos:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    '''add Inspo data to table'''
                inspo.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {Inspo.id}")
    
