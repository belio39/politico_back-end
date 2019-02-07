
# import unittest
# from app import app
# from app.API.v1.views.user_registration import *

# class BaseTest(unittest.TestCase):
#   def setUp(self):
#     self.app = app
#     self.client = self.app.test_client()
#     self.user_registration = {
#       "first_name": "belio", 
#       "last_name" : "dennis",
#       "other_name": "rotich", 
#       "email": "dbelio@gmail.com",
#       "phone_number": "+254723624569",
#       "passport": "passport",
#       "password": "123456",
#       }

#   def test_registration(self):
#     register = self.client.post('/users', data=self.user_registration)
#     self.assertEqual(register.status_code, 400)

#   def tearDown(self):
    
#     self.app = None

