
import unittest
from app import app

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.client = self.app.test_client()
    self.user_registration = {self, first_name, last_name, other_name, email, phone_number, passport_url, password}
    self.


  def tearDown(self):
    
    self.app = None
