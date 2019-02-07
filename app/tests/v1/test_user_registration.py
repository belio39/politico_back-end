
import unittest
from app import app
from app.API.v1.views.user_registration import *

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.user_registration_valid = {
      "first_name": "belio", 
      "last_name" : "dennis",
      "other_name": "rotich", 
      "email": "dbelio@gmail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "123456",
      }
  
    self.user_registration_invalid_email = {
      "first_name": "belio", 
      "last_name" : "dennis",
      "other_name": "rotich", 
      "email": "dbeliomail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "123456",
      }

    self.user_registration_no_first_name = {
      "first_name": "", 
      "last_name" : "dennis",
      "other_name": "rotich", 
      "email": "dbelio39@gmail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "123456",
      }

    self.user_registration_no_last_name = {
      "first_name": "belio", 
      "last_name" : "dennos",
      "other_name": "", 
      "email": "dbelio39@gmail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "123456",
      }
      
    self.user_registration_no_other_name = {
      "first_name": "belio", 
      "last_name" : "",
      "other_name": "rotich", 
      "email": "dbelio39@gmail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "123456",
      }

    self.user_registration_no_phone_number = {
      "first_name": "belio", 
      "last_name" : "",
      "other_name": "rotich", 
      "email": "dbelio39@gmail.com",
      "phone_number": "",
      "passport": "passport",
      "password": "123456",
      }
    self.user_registration_no_passport = {
      "first_name": "belio", 
      "last_name" : "dennis",
      "other_name": "rotich", 
      "email": "dbelio39@gmail.com",
      "phone_number": "+254723624569",
      "passport": "",
      "password": "123456",
      }

    self.user_registration_no_password = {
      "first_name": "belio", 
      "last_name" : "dennis",
      "other_name": "rotich", 
      "email": "dbelio39@gmail.com",
      "phone_number": "+254723624569",
      "passport": "passport",
      "password": "",
      }

  def test_registration_valid(self):
    register = self.client.post('/users', data=self.user_registration_valid)
    self.assertEqual(register.status_code, 400)

  def test_registration_invalid_email(self):
    register = self.client.post('/users', data=self.user_registration_invalid_email)
    self.assertEqual(register.status_code, 400)

  def test_registration_no_first_name(self):
    register = self.client.post('/users', data=self.user_registration_no_first_name)
    self.assertEqual(register.status_code, 400)
  
  def test_registration_no_last_name(self):
    register = self.client.post('/users', data=self.user_registration_no_last_name)
    self.assertEqual(register.status_code, 400)

  def test_registration_no_other_name(self):
    register = self.client.post('/users', data=self.user_registration_no_other_name)
    self.assertEqual(register.status_code, 400)
  
  def test_registration_no_phone_number(self):
    register = self.client.post('/users', data=self.user_registration_no_phone_number)
    self.assertEqual(register.status_code, 400)

  def test_registration_no_passport(self):
    register = self.client.post('/users', data=self.user_registration_no_passport)
    self.assertEqual(register.status_code, 400)

  def test_registration_no_password(self):
    register = self.client.post('/users', data=self.user_registration_no_password)
    self.assertEqual(register.status_code, 400)

  def tearDown(self):
      
    self.app = None

