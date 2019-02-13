import os
import re
from ..models.political_party import PartysModel, partys
from flask import Flask
from flask_restful import Resource, reqparse
from app import app, api
import werkzeug
from werkzeug.utils import secure_filename

political_party = reqparse.RequestParser()
political_party.add_argument('name', type=str, help='Please enter your name', required=True)
political_party.add_argument('headquateraddress', type=str, help='Please enter your headquateraddress', required=True)
political_party.add_argument('logo', type=werkzeug.datastructures.FileStorage, location='files', required=True)

edit_political_party = reqparse.RequestParser()
edit_political_party.add_argument('name', type=str, help='Please enter your name', required=True)
edit_political_party.add_argument('headquateraddress', type=str, help='Please enter your headquateraddress', required=True)
edit_political_party.add_argument('logo', type=werkzeug.datastructures.FileStorage, location='files', required=True)

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Party(Resource):
  
  def get(self):
   partys = PartysModel()
   if not partys.get_all_party():
      return {"status":404, "message": "There are no parties available at the moment"}, 404
   return {"status":200, "message":partys.get_all_party()}, 200

  def post(self):
    arguments = political_party.parse_args()
    name = arguments['name']
    headquateraddress = arguments['headquateraddress']
    logo = arguments['logo']

    if not name:
        return {"status":400, "message": "Please provide name"}, 400
    if not headquateraddress:
        return {"status":400, "message": "Please provide headquateraddress"}, 400
    if not re.match(r"^[A-Za-z0-9\.\+_-]*$", headquateraddress): 
      return {"status":400,"message": "Please provide a valid headquateraddress."}, 400  
    if logo:
      logo_url = secure_filename(logo.filename)
      logo.save(os.path.join(app.config['UPLOAD_FOLDER'], logo_url))
    if not name.isalpha():
      return{"status":400,"message":"Political name should only contain alphabets"}, 400
    if not logo_url:
      return {"status":400,"message": "Please provide logo_url"}, 400
    party = PartysModel()
    party = party.save(name, headquateraddress, logo_url)
    return {"status":201, "message":"Party created successfully" ,"data": party }, 201
class SingleParty(Resource):
  def get(self,party_id):
    single_party=PartysModel()
    if not single_party.get_single_party(party_id):
      return {"status":404,"message": "Party not found"}, 404
    return {"status":200, "message": single_party.get_single_party(party_id)}, 200
  
  def delete(self, party_id):
    party = PartysModel()
    single_party = party.get_single_party(party_id)
    if not single_party:
      return {"data":404, "message": "Party not found"}, 404
    party.delete_single_party(party_id)
    return {"status":200,"message": "Party deleted successfully"}, 200

  def patch(self, party_id):
    arguments = edit_political_party.parse_args()
    name = arguments['name']
    headquateraddress = arguments['headquateraddress']
    logo = arguments['logo']
    if logo:
      logo_url = secure_filename(logo.filename)
      logo.save(os.path.join(app.config['UPLOAD_FOLDER'], logo_url))
    party = PartysModel()
    find_party = party.get_single_party(party_id)
    if not find_party:
      return {"status":404,"message": "Party not found"}, 404
    par = party.edit_party(party_id, name, headquateraddress, logo_url)
    return {"status":200,"message": "Party edited successfully", "data": par}, 200

api.add_resource(Party, '/party')
api.add_resource(SingleParty, '/party/<int:party_id>')


