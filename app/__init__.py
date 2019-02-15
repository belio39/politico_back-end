
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

app.config['SECRET_KEY'] = '@#$%^&*()'

from app.API.v1.views.user_registration import *
from app.API.v1.views.political_party import *
from app.API.v1.views.political_office import *
