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
# class ISPE(db.Model):
   # __tablename__ = 'ISPE'

    # Define the Notes schema
   # id = db.Column(db.Integer, primary_key=True)
    #name2 = db.Column(db.Text, unique=False, nullable=False)
   # duration2 = db.Column(db.Integer, unique=False, nullable=False)
   # date2 = db.Column(db.Date)
    #grade = db.Column(db.Text, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
   # userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    #def __init__(self, id, name2, duration2, date2, grade):
       # self.userID = id
       # self.name2 = name2
       # self.duration2 = duration2
        #self.date2 = date2
        #self.grade = grade
    
    # FOR ISPE PAGE:
    # a getter method, extracts email from object
    #@property
    #def grade(self):
       # return self._grade
    
    # a setter function, allows name to be updated after initial object creation
    #@grade.setter
    #def grade(self, grade):
        #self._grade = grade

 # a getter method, extracts email from object
   # @property
    #def name2(self):
       # return self._name2
    
    # a setter function, allows name to be updated after initial object creation
   # @name2.setter
    #def name2(self, name2):
     #   self._name2 = name2
    
     # a getter method, extracts email from object
    #@property
    #def duration2(self):
    #    return self._duration2
    
    # a setter function, allows name to be updated after initial object creation
    #@duration2.setter
    #def duration2(self, duration2):
    #    self._duration2 = duration2
    
     # a getter method, extracts email from object
    #@property
    #def date2(self):
     #   return self._date2
    
    # a setter function, allows name to be updated after initial object creation
    #@date2.setter
    #def date2(self, date2):
     #   self._date2 = date2

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    #def __repr__(self):
        #return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
        #def create(self):
        #try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
         #   db.session.add(self)  # add prepares to persist person object to Notes table
          #  db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
           # return self
        #except IntegrityError:
         #   db.session.remove()
          #  return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    #def read(self):
        # encode image
        #path = app.config['UPLOAD_FOLDER']
        #file = os.path.join(path, self.image)
        #file_text = open(file, 'rb')
        #file_read = file_text.read()
        #file_encode = base64.encodebytes(file_read)
        
     #   return {
      #      "id": self.id,
       #     "userID": self.userID,
        #    "name2": self.name2,
         #   "duration2": self.duration2,
          #  "date2": self.date2,
           # "grade": self.grade
        #}

### INSPO 

# Define the inspo class to manage actions in 'inspo' table,  with a relationship to 'users' table
# class inspo(db.Model):
        #__tablename__ = 'inspo'

    # Define the Notes schema
    #id = db.Column(db.Integer, primary_key=True)
    #quote = db.Column(db.Text, unique=False, nullable=False)
    

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    #userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    #def __init__(self, id, quote):
       # self.userID = id
        #self.quote = quote
    
    # FOR INSPO PAGE:
    # a getter method, extracts email from object
   # @property
    #def quote(self):
       # return self._quote
    
    # a setter function, allows name to be updated after initial object creation
    #@quote.setter
    #def quote(self, quote):
        #self._quote = quote

    

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    #def __repr__(self):
        #return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
   # def create(self):
    #    try:
     #       # creates a Notes object from Notes(db.Model) class, passes initializers
      #      db.session.add(self)  # add prepares to persist person object to Notes table
       #     db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
        #    return self
        #except IntegrityError:
         #   db.session.remove()
          #  return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    #def read(self):
        # encode image
        #path = app.config['UPLOAD_FOLDER']
        #file = os.path.join(path, self.image)
        #file_text = open(file, 'rb')
        #file_read = file_text.read()
        #file_encode = base64.encodebytes(file_read)
        
     #   return {
      #      "id": self.id,
       #     "userID": self.userID,
        #    "quote": self.quote
        #}

### WORKOUTS


# Define the workouts class to manage actions in 'workouts' table,  with a relationship to 'users' table
class workouts(db.Model):
    __tablename__ = 'workouts'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.Text, unique=False, nullable=False)
    date = db.Column(db.Date)
    duration = db.Column(db.Integer, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, exercise, date, duration):
        self.userID = id
        self.exercise = exercise
        self.date = date
        self.duration = duration

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
            "userID": self.userID,
            "exercise": self.exercise,
            "duration": self.duration,
            "date": self.date
        }

## INPUTTED WORKOUT CLASS

class InputWork(db.Model):
    __tablename__ = 'InputWork'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    exerciseType = db.Column(db.Text, unique=False, nullable=False)
    sets = db.Column(db.Text, unique=False, nullable=False)
    reps = db.Column(db.Text, unique=False, nullable=False)

    
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    userID = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, exerciseType, sets, reps):
        self.userID = id
        self.exerciseType = exerciseType
        self.sets = sets
        self.reps = reps

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
            "userID": self.userID,
            "exerciseType": self.exerciseType,
            "sets": self.sets,
            "reps": self.reps
        }



### USERS

# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class User(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(255), unique=False, nullable=False)
    _dob = db.Column(db.Date)

    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    workouts = db.relationship("workouts", cascade='all, delete', backref='users', lazy=True)
    inspo = db.relationship("inspo", cascade='all, delete', backref='users', lazy=True)
    ISPE = db.relationship("ISPE", cascade='all, delete', backref='users', lazy=True)
    InputWork = db.relationship("InputWork", cascade='all, delete', backref='users', lazy=True)


    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, uid, password="123qwerty", dob=date.today()):
        self._name = name    # variables with self prefix become part of the object, 
        self._uid = uid
        self.set_password(password)
        self._dob = dob

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
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
    def password(self):
        return self._password[0:10] + "..." # because of security only show 1st characters

    # update password, this is conventional setter
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # check password parameter versus stored/encrypted password
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def dob(self):
        dob_string = self._dob.strftime('%m-%d-%Y')
        return dob_string
    
    # dob should be have verification for type date
    @dob.setter
    def dob(self, dob):
        self._dob = dob
    
    @property
    def age(self):
        today = date.today()
        return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
    
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
            "name": self.name,
            "uid": self.uid,
            "dob": self.dob,
            "age": self.age,
            "workouts": [workouts.read() for workouts in self.workouts],
            # "inspo": [inspo.read() for inspo in self.inspo],
            # "ISPE": [ISPE.read() for ISPE in self.ISPE],
            "InputWork": [InputWork.read() for InputWork in self.InputWork]
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", uid="", password=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(uid) > 0:
            self.uid = uid
        if len(password) > 0:
            self.set_password(password)
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
def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = User(name='Alexa Carlson', uid='alexa', password='123lex', dob=date(2006, 5, 16))
        u2 = User(name='Ava Carlson', uid='ava', password='123ava')
        u3 = User(name='Tom Holland', uid='tommy', password='123tom', dob=date(1996, 6, 1))
        u4 = User(name='Dylan Obrien', uid='dylan', password='123dyl', dob=date(1991, 8, 26))
        u5 = User(name='John Mortensen', uid='jm1021', dob=date(1959, 10, 21))

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                 # note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
                    user.workouts.append(workouts(id=user.id, exercise='burpees', duration='2', date=date(2023, 1, 20)))
                   # user.inspo.append(inspo(id=user.id, quote='Hard work beats talent when talent does not work hard'))
                    # user.ISPE.append(ISPE(id=user.id, name2='Alexa', duration2='3', date2=date(2023, 2, 2), grade='A'))
                    user.InputWork.append(InputWork(id=user.id, exerciseType='4x4s', sets='4', reps='12'))
                '''add user/workouts/inspo/ISPE/Inputted Workout data to table'''
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.uid}")