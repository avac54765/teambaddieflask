""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

### ISPE

# Define the ISPE class to manage actions in 'ISPE' table
class ISPE(db.Model):
    __tablename__ = 'ISPE'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _name2 = db.Column(db.String, unique=False, nullable=False)
    _duration2 = db.Column(db.Integer, unique=False, nullable=False)
    _date2 = db.Column(db.String)
    _grade = db.Column(db.String, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema 

    
    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, name2, duration2, date2, grade):
        self.userID = id
        self._uid = uid
        self._name2 = name2
        self._duration2 = duration2
        self._date2 = date2
        self._grade = grade
    
    
    # getter method
    @property
    def uid(self):
        return self._uid
    
    # setter function
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, uid):
        return self._uid == uid


     # getter method
    @property
    def name2(self):
        return self._name2
    
    # setter function
    @name2.setter
    def name2(self, name2):
        self._name2 = name2

     # getter method
    @property
    def duration2(self):
        return self._duration2
    
    # setter function
    @duration2.setter
    def duration2(self, duration2):
        self._duration2 = duration2
    
     # getter method
    @property
    def date2(self):
        return self._date2
    
    # setter function
    @date2.setter
    def date2(self, date2):
        self._date2 = date2
    
     # getter method
    @property
    def grade(self):
        return self._grade
    
    # setter function
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    
    
    

    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

   

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        # encode image
        #path = app.config['UPLOAD_FOLDER']
        #file = os.path.join(path, self.image)
        #file_text = open(file, 'rb')
        #file_read = file_text.read()
        #file_encode = base64.encodebytes(file_read)
        
        return {
            "id": self.id,
            "uid": self.uid,
            "name2": self.name2,
            "duration2": self.duration2,
            "date2": self.date2,
            "grade": self.grade
        }

    def update(self, uid='', duration2=''):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(duration2) > 0:
            self.duration2 = duration2
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
def initISPEs():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = ISPE(id='33', name2='Alexa Carlson', uid='alexa', duration2='2', date2=date(2006, 5, 16), grade='A')
        i2 = ISPE(id='24', name2='Ava Carlson', uid='ava', duration2='5', date2=date(2007, 5, 16), grade='A')
        i3 = ISPE(id='56', name2='Tom Holland', uid='tommy', duration2='3', date2=date(1996, 6, 1), grade='B')
        i4 = ISPE(id='23', name2='Dylan Obrien', uid='dylan', duration2='4', date2=date(1991, 8, 26), grade='D')
        i5 = ISPE(id='59', name2='John Mortensen', uid='jm1021', duration2='1', date2=date(1959, 10, 21), grade='A')

        ispes = [i1, i2, i3, i4, i5]

        """Builds sample user/note(s) data"""
        for ispe in ispes:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                    '''add ISPE data to table'''
                    ispe.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {ISPE.id}")
    
