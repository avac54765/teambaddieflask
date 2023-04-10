from flask import Flask, render_template, url_for, redirect, Blueprint, request, jsonify, make_response, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
import random
import requests
import string
import json 
import http.cookies as cookies


app = Flask(__name__) 
#Creates a flask application instance and assigns it to the variable flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
# Sets configuration for SQLAlchemy specifying database URI 
bcrypt = Bcrypt(app)
# hashed-passwords
db = SQLAlchemy(app) #Creates and instance of SQAlchemy and assigns it to db and this is used to interact with the database. app.config['SECRET_KEY'] = 'thisisasecretkey' # This is a secret key for the flask
app.config['SECRET_KEY'] = 'thisisasecretkey'
#secret key for the flask
pass_api = Blueprint('pass_api', __name__, url_prefix='/api/pass')
api = Api(pass_api)
app.register_blueprint(pass_api)


login_manager = LoginManager()
# This line creates an instance of the LoginManager class from the flask_login library
login_manager.init_app(app)
# This line initializes the LoginManager instance with your Flask application, app. 
# This is required in order to use the functionality provided by flask_login.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# The load_user function takes a single argument user_id which is the user's identifier.
# The function returns a user object obtained by querying the User model for the user with the specified user_id. 
# The user object is then stored in the current session,  allowing the application to keep track of the user's identity and state between requests.

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
#used to store user information in the database


# This function is to Verify if token is valid, Signature portion of the token
def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       # Grabs the cookie from request  headers
       cookieString = request.headers.get('Cookie')
       # loads the cookie into cookie object
       if cookieString:
           cookie = cookies.SimpleCookie()
           cookie.load(cookieString)
            # if token exist then it grabs the token from the cookie
           if 'token' in cookie:
               token = cookie['token'].value
 
        # if no token exits it shows a message saying valid token is missing 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
        # this code tries to verify the signature of the token by decoding it.
       try:
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           current_user = User.query.filter_by(username=data['name']).first()
        # if signature is not valid or it is not able to decode it writes a message saying token is invalid. 
       except:
           return jsonify({'message': 'token is invalid'})
        # returns current user
       return f(current_user, *args, **kwargs)
       # returns the decorator
   return decorator


# This code is actually a special function. This function will create a custom decorator with the code required to create and validate tokens. Python provides a very amazing feature named function decorators. These function decorators allow very neat features for web development. In Flask, each view is considered as a function, and decorators are used for injecting additional functionality to one or more functions. In this case, the functionality handled by this custom decorator will be to create and validate tokens.



class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    show_password = BooleanField('Show Password')

    submit = SubmitField('Register')


    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'The username already exists. Please choose a different username.')
#This checks if there is already a username in the database and if there is it asks the user to choose a different username

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')



@app.route('/')
def home():
    return render_template('home.html')
# Link to home page



@ app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegisterForm()
   if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data)
       new_user = User(username=form.username.data, password=hashed_password)
       db.session.add(new_user)
       db.session.commit()
       return redirect(url_for('login'))


   return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    # loads login form
    form = LoginForm()
    # when user submits information it creates a token (this is where a token is created and stored in a cookie)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # checks the user entered password against the database stored password
            if bcrypt.check_password_hash(user.password, form.password.data):
                # This is were token is created . Takes the payload with username and encodes using the secret key and algorithm(HS256).
                token = jwt.encode(payload= {'name': user.username}, key=app.config['SECRET_KEY'], algorithm="HS256")
                # calls for dashboad url
                response = make_response(redirect(url_for('dashboard')))
                # sets the token in a cookie
                response.set_cookie('token', token) 
                # return response back to client 
                return response
        # if validation is not succesful it goes back to log in page
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)










@app.route('/generate_password', methods=['GET'])
def getPassAPI(length=3):
  password = []
  url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
  querystring = {"count": str(length)}
  headers = {
      "X-RapidAPI-Key": "f0aeb431bamshc18b522b64e7383p102f67jsnea4673acfc55",
      "X-RapidAPI-Host": "random-words5.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  words = response.json()
  password += words
  num_random_chars = (length * 2) - len(words)
  password += [random.choice(string.ascii_letters + string.digits) for i in range(num_random_chars)]
  random.shuffle(password)
  response = ''.join(password)
  return response




@app.route('/generate_random_password')
def index():
  password = getPassAPI(5)  # generate password of length 5
  save_to_json(password)
  return render_template('genpass.html', password=password)




class PassAPI:
  class _Read(Resource):
      def get(self):
          return getPassAPI()




  api.add_resource(_Read, '/')




def save_to_json(password):
  # open the JSON file in write mode
  with open('passwords.json', 'w') as f:
      # write the password to the file as a JSON object
      json.dump({"password": password}, f)




# call the function to save the password to the JSON file
save_to_json(getPassAPI(7))  # generate password of length 7












@app.route('/dashboard', methods=['GET', 'POST'])
#token required to access this page, ONLY once token is validated this page can be accesed at all times. 
@token_required
def dashboard(temp):
    return render_template('dashboard.html')
# This redirects to dashboard page ones loged in, and log in succesful is required.

@app.route('/logout', methods=['GET', 'POST'])
@token_required
def logout(temp):
    logout_user()
    response = make_response(redirect(url_for('login')))
    response.set_cookie('token', expires=0)
    return response

# Logout and redirects you back to log in







if __name__ == "__main__":
    app.run(debug=True)
# Enables flask debug mode



