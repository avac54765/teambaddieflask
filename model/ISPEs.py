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

# Define the ISPE class to manage actions in 'ISPE' table,  with a relationship to 'users' table
class ISPE(db.Model):
    __tablename__ = 'ISPE'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _name2 = db.Column(db.Text, unique=False, nullable=False)
    _duration2 = db.Column(db.Integer, unique=False, nullable=False)
    _date2 = db.Column(db.Date)
    _grade = db.Column(db.Text, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, name2, duration2, date2, grade):
        self.userID = id
        self._uid = uid
        self.name2 = name2
        self.duration2 = duration2
        self.date2 = date2
        self.grade = grade
    
        # FOR ISPE PAGE:
    # a getter method, extracts email from object
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
    def id(self):
        return self._id
    
    # a setter function, allows name to be updated after initial object creation
    @id.setter
    def id(self, id):
        self._id = id
    
     # a getter method, extracts email from object
    @property
    def name2(self):
        return self._name2
    
    # a setter function, allows name to be updated after initial object creation
    @name2.setter
    def name2(self, name2):
        self._name2 = name2

     # a getter method, extracts email from object
    @property
    def duration2(self):
        return self._duration2
    
    # a setter function, allows name to be updated after initial object creation
    @duration2.setter
    def duration2(self, duration2):
        self._duration2 = duration2
    
     # a getter method, extracts email from object
    @property
    def date2(self):
        return self._date2
    
    # a setter function, allows name to be updated after initial object creation
    @date2.setter
    def date2(self, date2):
        self._date2 = date2
    
     # a getter method, extracts email from object
    @property
    def grade(self):
        return self._grade
    
    # a setter function, allows name to be updated after initial object creation
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    
    
    
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
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        i1 = ISPE(name2='Alexa Carlson', uid='alexa', duration2='2', date2=date(2006, 5, 16), grade='A')
        i2 = ISPE(name2='Ava Carlson', uid='ava')
        i3 = ISPE(name2='Tom Holland', uid='tommy', duration2='3', date2=date(1996, 6, 1), grade='B')
        i4 = ISPE(name2='Dylan Obrien', uid='dylan', duration2='4', date2=date(1991, 8, 26), grade='D')
        i5 = ISPE(name2='John Mortensen', uid='jm1021', duration2='1', date2=date(1959, 10, 21), grade='A')

        ISPEs = [i1, i2, i3, i4, i5]

        """Builds sample user/note(s) data"""
        for ISPE in ISPEs:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    '''add ISPE data to table'''
                    ISPE.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {ISPE.id}")
    
