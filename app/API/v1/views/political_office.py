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
    name = arguments['name']

    if not office_type or not name:
      return{"message": "Provide office and name"}, 400

    if not office_type.isalpha():
      return{"message":"Office type should be alphabet"}, 400

    for office in offices:
      if office_type in office.values() or name in office.values():
        return {"message": "either office or name already exists"}, 400

    office = OfficesModel()
    office = office.save(office_type, name)
    return {"message": "Office created successfully" ,"data": [office] }, 201

class SingleOffice(Resource):
  def get(self,id):
    single_office = OfficesModel()
    if not single_office.single_office(id):
      return {"message": "page not availabe"}, 400
    return single_office.single_office(id), 201

class GetAllOffice(Resource):
  def get(self):
    office = OfficesModel()
    if not office.all_office():
      return {"message": "page not availabe"}, 400
    return office.all_office()
    
api.add_resource(Office, '/office')
api.add_resource(SingleOffice, '/office/<int:id>')
api.add_resource(GetAllOffice, '/offices')

