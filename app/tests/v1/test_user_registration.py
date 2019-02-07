from app import app
import unittest

testapp = app.test_client()

class TestUserRegistration(unittest.TestCase):
  def users(self,first_name, last_name, other_name, email, phone_number, passport_url, password):
    return testapp.post('/users',data=dict(first_name=first_name,
    last_name = last_name , other_name = other_name, email=email,
    phone_number=phone_number,passport_url = passport_url),follow_redirects=True)

