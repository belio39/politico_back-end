import unittest
from app import app
from app.API.v1.views.political_party import *

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.test_political_party_valid = {
      "name": "belio", 
      "hq_address" : "dennis",
      "logo_url": "rotich", 
    }

    self.test_political_party_with_no_name = {
        "name": "", 
        "hq_address" : "dennis",
        "logo_url": "rotich",
    }

    self.test_political_party_with_no_hq_address = {
        "name": "belio", 
        "hq_address" : "dennis",
        "logo_url": "rotich", 
    }

    self.test_political_party_with_no_logo_url = {
        "name": "belio", 
        "hq_address" : "dennis",
        "logo_url": "", 
    }
    
  def test_political_party_valid(self):
    register = self.client.post('/party', data=self.test_political_party_valid)
    self.assertEqual(register.status_code, 400)  
  
  def test_political_party_with_no_name(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_name)
    self.assertEqual(register.status_code, 400)  

  def test_political_party_with_no_hq_address(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_hq_address)
    self.assertEqual(register.status_code, 400)

  def test_political_party_with_no_logo_url(self):
    register = self.client.post('/party', data=self.test_political_party_with_no_logo_url)
    self.assertEqual(register.status_code, 400)  

  def tearDown(self):
      
    self.app = None  
