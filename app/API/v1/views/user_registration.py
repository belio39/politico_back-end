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
user_registration.add_argument('firstname', type=str,
                               help='Please enter your first name',
                               required=True)
user_registration.add_argument('lastname', type=str,
                               help='Please enter your last name',
                               required=True)
user_registration.add_argument('othername', type=str,
                               help='Please enter your other name')
user_registration.add_argument('email', type=str,
                               help='Please enter your email',
                               required=True)
user_registration.add_argument('phonenumber', type=str,
                               help='Please enter your phone number',
                               required=True)
user_registration.add_argument('passporturl',
                               type=werkzeug.datastructures.FileStorage,
                               location='files', required=True)
user_registration.add_argument('password', type=str,
                               help='Please provide your password',
                               required=True)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Main(Resource):
    def get(self):
        return{"status": 200, "message": "Main page"}, 200


class Users(Resource):
    def post(self):
        arguments = user_registration.parse_args()
        firstname = arguments['firstname'].strip()
        lastname = arguments['lastname'].strip()
        othername = arguments['othername']
        email = arguments['email']
        phonenumber = arguments['phonenumber']
        passporturl = arguments['passporturl']
        password = arguments['password']

        if passporturl:
            checkpassporturl = secure_filename(passporturl.filename)
            passporturl.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                          checkpassporturl))
        if not firstname:
            return {"status": 400, "message": "Please provide first name"}, 400

        if not lastname:
            return{"status": 400, "message": "Please provide first name"}, 400

        if not email:
            return{"status": 400, "message": "Please provide email"}, 400

        if not phonenumber:
            return{"status": 400, "message":
                   "Please provide phone number"}, 400

        if not passporturl:
            return{"status": 400, "message": "Please provide passport"}, 400
        if not re.match('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])',
                        password):
            return {"status": 400, "message": "Invalid password"}, 400

        if not len(phonenumber) == 13:
            return{"status": 400, "message":
                   "Phone must have 12 character"}, 400

        if not phonenumber.startswith('+254') or not phonenumber[1:13].isdigit():
            return {"status": 400, "message":
                    "Please provide a valid phone number,"
                    "start with +254"}, 400

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
                        email):
            return {"status": 400, "message":
                    "Please provide a valid email."}, 400

        for user in users:
            if email in user.values():
                return {"status": 409, "message": "Email already exists"}, 409
            if phonenumber in user.values():
                return {"status": 409, "message":
                        "Phone number already exists"}, 409

        hashed_password = generate_password_hash(password)
        new_user = UsersModel(firstname, lastname, othername, email,
                              phonenumber, checkpassporturl, hashed_password)
        new_user = new_user.save(firstname, lastname, othername,
                                 email, phonenumber, checkpassporturl,
                                 hashed_password)
        return {"status": 201, "data": new_user}, 201

api.add_resource(Users, '/users')
api.add_resource(Main, '/')
