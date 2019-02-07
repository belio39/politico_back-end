import unittest
from app import app

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.app=app
    self.client = self.app.test_client()

  def tearDown(self):
    self.app=None    
