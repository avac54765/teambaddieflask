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
class workout(db.Model):
    __tablename__ = 'workout'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _name3 = db.Column(db.String, unique=False, nullable=False)
    _duration = db.Column(db.Integer, unique=False, nullable=False)
    _date = db.Column(db.String)
    _type = db.Column(db.String, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    # userID = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, name3, duration, date, type):
        self.userID = id
        self._uid = uid
        self._name3 = name3
        self._duration = duration
        self._date = date
        self._type = type
    
        # FOR ISPE PAGE:
    # a getter method
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

    #@property
    #def id(self):
       # return self._id
    
    # a setter function, allows id to be updated after initial object creation
    #@id.setter
    #def id(self, id):
       # self._id = id
    
     # a getter method
    @property
    def name3(self):
        return self._name3
    
    # a setter function, allows name to be updated after initial object creation
    @name3.setter
    def name3(self, name3):
        self._name3 = name3

     # a getter method
    @property
    def duration(self):
        return self._duration
    
    # a setter function, allows duration to be updated after initial object creation
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
     # a getter method
    @property
    def date(self):
        return self._date
    
    # a setter function, allows date to be updated after initial object creation
    @date.setter
    def date(self, date):
        self._date = date
    
     # a getter method
    @property
    def type(self):
        return self._type
    
    # a setter function, allows grade to be updated after initial object creation
    @type.setter
    def type(self, type):
        self._type = type
    
    
    
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

   

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    #def __repr__(self):
        #return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

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
            "name3": self.name3,
            "duration": self.duration,
            "date": self.date,
            "type": self.type
        }

    def update(self, uid='', duration=''):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(duration) > 0:
            self.duration = duration
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
def initworkouts():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = workout(id='33', name3='Alexa Carlson', uid='alexa', duration='2', date=date(2006, 5, 16), type='swimming')
        i2 = workout(id='24', name3='Ava Carlson', uid='ava', duration='5', date=date(2007, 5, 16), type='running')
        i3 = workout(id='56', name3='Tom Holland', uid='tommy', duration='3', date=date(1996, 6, 1), type='basketball')
        i4 = workout(id='23', name3='Dylan Obrien', uid='dylan', duration='4', date=date(1991, 8, 26), type='running')
        i5 = workout(id='59', name3='John Mortensen', uid='jm1021', duration='1', date=date(1959, 10, 21), type='walking')

        workouts = [i1, i2, i3, i4, i5]

        """Builds sample user/note(s) data"""
        for workout in workouts:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    '''add ISPE data to table'''
                    workout.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {workout.id}")
    