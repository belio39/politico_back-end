import unittest
from app import app
from app.API.v1.views.political_office import *

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.test_political_office_valid = {
      "office_type": "mhyughp", 
      "name" : "khganu",
    }

    self.test_political_office_taken_inputs = {
      "office_type" : "mp",
      "name" : "kanu",
    }

    self.test_political_office_empty_fields = {
      "office_type" : "",
      "name" : "",
    }

    self.test_political_office_not_isalpha = {
      "office_type" : "@#$%^&*@!98ty",
      "name" : "KANU",
    }  

  def test_political_office_valid(self):
    register = self.client.post('/office', data=self.test_political_office_valid, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 201)   

  def test_political_office_taken_inputs(self):
    register = self.client.post('/office', data=self.test_political_office_taken_inputs, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_political_office_empty_fields(self):
    register = self.client.post('/office', data=self.test_political_office_empty_fields, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_political_office_not_isalpha(self):
    register = self.client.post('/office', data=self.test_political_office_not_isalpha, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400) 
