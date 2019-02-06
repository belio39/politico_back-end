import re
import os
from ..models.political_party import PartysModel, partys
from flask import Flask
from flask_restful import Resource, reqparse
from app import app, api
import werkzeug
from werkzeug.utils import secure_filename

political_party = reqparse.RequestParser()
political_party.add_argument('name', type=str, help='Please enter your name', required=True)
political_party.add_argument('hq_address', type=str, help='Please enter your hq_address', required=True)
political_party.add_argument('logo', type=werkzeug.datastructures.FileStorage, location='files', required=True)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Party(Resource):
  def post(self):
    arguments = political_party.parse_args()
    name = arguments['name']
    hq_address = arguments['hq_address']
    logo = arguments['logo']

    for party in partys:  
      if name in party.values():
        return {"message": "political party already exists"}, 400
    if logo:
      logo_url = secure_filename(logo.filename)
      logo.save(os.path.join(app.config['UPLOAD_FOLDER'], logo_url))
    if not name.isalpha():
      return{"message":"Bad format"}, 400
    if not name or not hq_address or not logo_url:
      return {"message": "Please provide name or hq_address or logo_url"}, 400
    party = PartysModel(name, hq_address, logo_url)
    party = party.save(name, hq_address, logo_url)
    return {"message": "Party created successfully" ,"data": [party] }, 200

api.add_resource(Party, '/party')


