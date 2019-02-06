import re
from ..models.political_office import OfficesModel, offices
from flask import Flask
from flask_restful import Resource, reqparse
from app import app, api

political_office = reqparse.RequestParser()
political_office.add_argument('office_type', type=str, help='Please enter your office_type', required=True)
political_office.add_argument('name', type=str, help='Please enter your name', required=True)

class Office(Resource):
  def post(self):
    arguments = political_office.parse_args()
    office_type = arguments['office_type']
    if re.match (r"^[0-9\.\+_*&#@$%()?|[]]", office_type):
      return{"message":"Bad format"}
    name = arguments['name']
    if not office_type.isalpha():
      return{"message":"Bad format"}
    if not office_type or not name:
      return{"message": "Provide office and name"}, 400
    for office in offices: 
      if office_type in office.values():
        return {"message": "office already exists"}, 400
      if name in office.values():
        return {"message": "name already exists"}     
    office = OfficesModel(office_type, name)
    office = office.save(office_type, name)
    return {"message": "Office created successfully" ,"data": [office] }, 200  

api.add_resource(Office, '/office')    
