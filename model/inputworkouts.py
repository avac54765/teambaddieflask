""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



## INPUTTED WORKOUT CLASS


class InputWork(db.Model):
    __tablename__ = 'inputworkouts'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _exerciseType = db.Column(db.Text, unique=False, nullable=False)
    _sets = db.Column(db.Text, unique=False, nullable=False)
    _reps = db.Column(db.Text, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    # userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, exerciseType, sets, reps):
        self.userID = id
        self._uid = uid
        self.exerciseType = exerciseType
        self.sets = sets
        self.reps = reps


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


    @property
    def exerciseType(self):
        return self._exerciseType
    
    # a setter function, allows name to be updated after initial object creation
    @exerciseType.setter
    def exerciseType(self, exerciseType):
        self._exerciseType = exerciseType


    @property
    def sets(self):
        return self._sets
    
    # a setter function, allows name to be updated after initial object creation
    @sets.setter
    def sets(self, sets):
        self._sets = sets


    @property
    def reps(self):
        return self._reps
    
    # a setter function, allows name to be updated after initial object creation
    @reps.setter
    def reps(self, reps):
        self._reps = reps

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
            "exerciseType": self.exerciseType,
            "sets": self.sets,
            "reps": self.reps
        }
    
    def update(self,sets=""):
        """only updates values with length"""
        if len(sets) > 0:
            self.sets = sets
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    

def initinputworkouts():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        i1 = InputWork(exerciseType='Frenchies', uid='alexa', sets='2', reps='3')
        i2 = InputWork(exerciseType='Symmetric Moves', id='ava', sets='3', reps='6-8')
        i3 = InputWork(exerciseType='Deadhangs', uid='lydia', sets='3', reps='15')
        i4 = InputWork(exerciseType='Lock-Offs', uid='sri', sets='3', reps='3')
        
        inputworkouts = [i1, i2, i3, i4]

        """Builds sample user/note(s) data"""
        for InputWork in inputworkouts:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    '''add inputted workout data to table'''
                InputWork.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"ERROR {InputWork.id}")
