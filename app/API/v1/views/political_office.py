from ..models.political_office import OfficesModel, offices
from flask import Flask
from flask_restful import Resource, reqparse
from app import app, api

political_office = reqparse.RequestParser()
political_office.add_argument('officetype', type=str,
                              help='Please enter your officetype',
                              required=True)
political_office.add_argument('name', type=str,
                              help='Please enter your name',
                              required=True)


class Office(Resource):
    def post(self):
        arguments = political_office.parse_args()
        officetype = arguments['officetype']
        name = arguments['name']

        if not officetype:
            return{"status": 400, "message": "Please provide office name"}, 400

        if not name:
            return{"status": 400, "message": "Please provide name"}, 400

        if not officetype.isalpha():
            return{"status": 400,
                   "message": "Office type should be alphabet"}, 400

        if not name.isalpha():
            return {"status": 400,
                    "message": "Name type should be alphabet"}, 400

        for office in offices:
            if officetype in office.values() or name in office.values():
                return {"status": 409,
                        "message": "either office or name already exists"}, 409

        office = OfficesModel()
        office = office.save(officetype, name)
        return {"status": 201, "data": [office]}, 201


class SingleOffice (Resource):

    def get(self, id):
        single_office = OfficesModel()
        if not single_office.single_office(id):
            return {"status": 404,
                    " message": "No office availabe now please try later"}, 404
        return {"status": 201, "data": single_office.single_office(id)}, 201


class GetAllOffice(Resource):

    def get(self):
        office = OfficesModel()
        if not office.all_office():
            return {"status": 404,
                    "message": "No offices availabe now please try later"}, 404
        return {"status": 200, "data": office.all_office()}, 200

api.add_resource(Office, '/offices')
api.add_resource(SingleOffice, '/offices/<int:id>')
api.add_resource(GetAllOffice, '/offices')
