
import unittest
from app import app
from io import BytesIO
from app.API.v1.views.user_registration import *


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.registration_valid = {
          "firstname": "belio",
          "lastname": "dennis",
          "othername": "rotich",
          "email": "dbelio@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": (BytesIO(b'file content'), "test.png"),
          "password": "1234tTR%&i56",
          }

        self.registration_invalid_email = {
          "firstname": "belio",
          "lastname": "dennis",
          "othername": "rotich",
          "email": "dbeliomail.com",
          "phonenumber": "+254723624569",
          "passporturl": "passport",
          "password": "123456",
          }

        self.registration_no_first_name = {
          "firstname": "",
          "lastname": "dennis",
          "othername": "rotich",
          "email": "dbelio39@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": "passport",
          "password": "123456",
          }

        self.registration_no_last_name = {
          "firstname": "belio",
          "lastname": "dennos",
          "othername": "",
          "email": "dbelio39@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": "passport",
          "password": "123456",
          }

        self.registration_no_other_name = {
          "firstname": "belio",
          "lastname": "",
          "othername": "rotich",
          "email": "dbelio39@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": "passport",
          "password": "123456",
          }

        self.registration_no_phone_number = {
          "firstname": "belio",
          "lastname": "",
          "othername": "rotich",
          "email": "dbelio39@gmail.com",
          "phonenumber": "",
          "passporturl": "passport",
          "password": "123456",
          }
        self.registration_no_passport = {
          "firstname": "belio",
          "lastname": "dennis",
          "othername": "rotich",
          "email": "dbelio39@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": "",
          "password": "123456",
          }

        self.registration_no_password = {
          "firstname": "belio",
          "lastname": "dennis",
          "othername": "rotich",
          "email": "dbelio39@gmail.com",
          "phonenumber": "+254723624569",
          "passporturl": "passport",
          "password": "",
          }

    def test_registration_valid(self):
        register = self.client.post('/users', data=self.registration_valid,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 201)

    def test_registration_invalid_email(self):
        register = self.client.post('/users',
                                    data=self.registration_invalid_email)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_first_name(self):
        register = self.client.post('/users',
                                    data=self.registration_no_first_name)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_last_name(self):
        register = self.client.post('/users',
                                    data=self.registration_no_last_name)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_other_name(self):
        register = self.client.post('/users',
                                    data=self.registration_no_other_name)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_phone_number(self):
        register = self.client.post('/users',
                                    data=self.registration_no_phone_number)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_passport(self):
        register = self.client.post('/users',
                                    data=self.registration_no_passport)
        self.assertEqual(register.status_code, 400)

    def test_registration_no_password(self):
        register = self.client.post('/users',
                                    data=self.registration_no_password)
        self.assertEqual(register.status_code, 400)

    def tearDown(self):

        self.app = None
