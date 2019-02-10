import unittest
from app import app
from io import BytesIO
from app.API.v1.views.political_party import *

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.test_political_party_valid = {
      "name": "belio", 
      "hq_address" : "dennis",
      "logo": (BytesIO(b'file content'),"test.png"),
    }
    self.test_political_party_taken_inputs = {
      "name" : "deni",
      "hq_address" : "kenya",
      "logo_url": "logo_url",
    }

    self.test_political_party_with_no_name = {
        "name": "", 
        "hq_address" : "dennis",
        "logo": "rotich",
    }

    self.test_political_party_with_no_hq_address = {
        "name": "belio", 
        "hq_address" : "dennis",
        "logo": "rotich", 
    }

    self.test_political_party_with_no_logo_url = {
        "name": "belio", 
        "hq_address" : "dennis",
        "logo": "", 
    }
    self.test_post_political_party_with_missing_fields = {
        "name": "", 
        "hq_address" : "",
        "logo": "", 
    }



    self.test_put_political_party_with_missing_fields = {
        "name": "", 
        "hq_add5645ress" : "",
        "logo": "", 
    }

    self.test_put_political_party_with_valid_fields = {
        "name": "belio", 
        "hq_address" : "dennis",
        "logo": (BytesIO(b'file content'),"test.png"),
    }


  def test_political_party_taken_inputs(self):
    register = self.client.post('/party', data=self.test_political_party_taken_inputs, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_political_party_valid(self):
    register = self.client.post('/party', data=self.test_political_party_valid, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 201)  
  
  def test_political_party_with_no_name(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_name, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_post_political_party_with_missing_fields(self):
    register = self.client.post('/party', data=self.test_post_political_party_with_missing_fields, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)  

  def test_put_political_party_with_missing_fields(self):
    register = self.client.put('/party/1', data=self.test_put_political_party_with_missing_fields, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_put_political_party_with_valid_fields(self):
    register = self.client.put('/party/1', data=self.test_put_political_party_with_valid_fields, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 200)  

  def test_delete_political_party_with_missing_fields(self):
    register = self.client.delete('/party/8')
    self.assertEqual(register.status_code, 404)

  def test_delete_political_party_with_valid_fields(self):
    register = self.client.delete('/party/1')
    self.assertEqual(register.status_code, 200)   
  
  def test_political_party_with_no_hq_address(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_hq_address, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)

  def test_political_party_with_no_logo(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_logo_url, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 400)  

  def test_political_party_with_no_logo(self):
    register = self.client.post('/get', data=self.test_political_party_with_no_logo_url, content_type='multipart/form-data')
    self.assertEqual(register.status_code, 404)
  
  def get_single_political_party(self):
    return self.client.get('/party/1')
  
  def get_single_political_party(self):
    response = get_single_political_party()
    self.assertEqual(response.status_code, 200)

  def get_all_political_party(self):
    return self.client.get('/party')

  def get_all_political_party(self):
    response = get_all_political_party()
    self.assertEqual(response.status_code, 200)

  def edit_political_party(self):
    return self.client.get('/party/8')

  def delete_political_party(self):
    return self.client.delete('/politics/1')

  def edit_political_party(self):
    response = edit_political_party()
    self.assertEqual(response.status_code, 200)

  def delete_political_party(self):
      return self.client.delete('/politics/1')

  def delete_political_party(self):
    response = delete_political_party()
    self.assertEqual(response.status_code, 200)

  def tearDown(self):
      
    self.app = None  





