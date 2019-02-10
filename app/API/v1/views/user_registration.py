import re
import os
from ..models.user_registration_model import UsersModel, users
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
from app import app, api
import werkzeug

user_registration = reqparse.RequestParser()
user_registration.add_argument('first_name', type=str, help='Please enter your first name', required=True)
user_registration.add_argument('last_name', type=str, help='Please enter your last name', required=True)
user_registration.add_argument('other_name', type=str, help='Please enter your other name', required=True)
user_registration.add_argument('email', type=str, help='Please enter your email', required=True)
user_registration.add_argument('phone_number', type=str, help='Please enter your phone_number', required=True)
user_registration.add_argument('passport', type=werkzeug.datastructures.FileStorage, location='files', required=True)
user_registration.add_argument('password', type=str, help='Please provide your password', required=True)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Main(Resource):
  def get(self):
    return{"message":"Main page"}, 200

class Users(Resource):
  '''User registration'''
  def post(self):
    arguments = user_registration.parse_args()
    first_name = arguments['first_name']
    last_name = arguments['last_name']
    other_name = arguments['other_name']
    email = arguments['email']
    phone_number = arguments['phone_number']
    passport = arguments['passport']
    password = arguments['password']
  
    if passport:
      passport_url = secure_filename(passport.filename)
      passport.save(os.path.join(app.config['UPLOAD_FOLDER'], passport_url))
    if not first_name or not last_name or not other_name or not email or not phone_number or not passport_url or not password:
      return {"message": "Please provide first_name or last_name or other_name or email or phone_number or passport_url"}, 400
    if len(password) < 6:
      return {"message": "Password length should be greater than 6"}, 400
    if not phone_number.startswith('+254'):
      return {"message": "Phone number must start with +254"}, 400
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
      return {"message": "Please provide a valid email."}, 400
    for user in users:
      if email in user.values() or phone_number in user.values():
        return {"message": "Email or phonr_number already exists"}, 409

    hashed_password = generate_password_hash(password)
    new_user = UsersModel(first_name, last_name, other_name, email, phone_number, passport_url, hashed_password)
    new_user = new_user.save(first_name, last_name, other_name, email, phone_number, passport_url, hashed_password)  
    return new_user, 201  

api.add_resource(Users, '/users')
api.add_resource(Main, '/')


