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
class workout(db.Model):
    __tablename__ = 'workout'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _fname = db.Column(db.String, unique=False, nullable=False)
    _lname = db.Column(db.String, unique=False, nullable=False)
    _workouttype = db.Column(db.String, unique=False, nullable=False)
    _duration = db.Column(db.Integer, unique=False, nullable=False)
    _date = db.Column(db.String)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    # userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, uid, fname, lname, workouttype, duration, date):
        self.userID = id
        self._uid = uid
        self._fname = fname
        self._lname = lname
        self._workouttype = workouttype
        self._duration = duration
        self._date = date
    
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

    # @property
    # def id(self):
        # return self._id
    
    # a setter function, allows name to be updated after initial object creation
    # @id.setter
    # def id(self, id):
        # self._id = id

    @property
    def fname(self):
        return self._fname
    
    # a setter function, allows name to be updated after initial object creation
    @fname.setter
    def fname(self, fname):
        self._fname = fname
    
     # a getter method, extracts email from object
    @property
    def lname(self):
        return self._lname
    
    # a setter function, allows name to be updated after initial object creation
    @lname.setter
    def lname(self, lname):
        self._lname = lname

     # a getter method, extracts email from object
    @property
    def workouttype(self):
        return self._workouttype
    
    # a setter function, allows name to be updated after initial object creation
    @workouttype.setter
    def workouttype(self, workouttype):
        self._workouttype = workouttype
    
     # a getter method, extracts email from object
    @property
    def duration(self):
        return self._duration
    
    # a setter function, allows name to be updated after initial object creation
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
     # a getter method, extracts email from object
    @property
    def date(self):
        return self._date
    
    # a setter function, allows name to be updated after initial object creation
    @date.setter
    def date(self, date):
        self._date = date
    
    
    
    
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
            "first name": self.fname,
            "last name": self.lname,
            "type of workout": self.workouttype,
            "duration": self.duration,
            "date": self.date
        }

    def update(self, uid='', workouttype=""):
        """only updates values with length"""
        if len(uid) > 0:
            self.uid = uid
        if len(workouttype) > 0:
            self.workouttype = workouttype
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
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        w1 = workout(id='12', fname='Sumedh', uid='sumedh', lname='Kotturi', workouttype='swimming', date=date(2006, 5, 16), duration='2')
        w2 = workout(id='13', fname='Srihita', uid='srihita', lname='Kotturi', workouttype='running', date=date(2006, 5, 16), duration='1')
        w3 = workout(id='8', fname='Chandram', uid='chandram', lname='Kotturi', workouttype='walking', date=date(2006, 5, 16), duration='3')
        w4 = workout(id='23', fname='Lalitha', uid='lalitha', lname='Chittila', workouttype='walking', date=date(2006, 5, 16), duration='1')
        w5 = workout(id='38', fname='Shashank', uid='shashank', lname='Mahavrathajula', workouttype='Basketball', date=date(2006, 5, 16), duration='4')

        Workouts = [w1, w2, w3, w4, w5]

        """Builds sample user/note(s) data"""
        for Workout in Workouts:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    '''add Workout data to table'''
                Workout.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {workout.id}")
    