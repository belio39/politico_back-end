import unittest
from app import app
from app.API.v1.views.political_office import *


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.test_political_offices_valid = {
         "officetype": "state",
         "name": "mca",
        }

        self.test_offices_taken_inputs = {
         "officetype": "mp",
         "name": "kanu",
        }

        self.test_offices_empty_fields = {
         "officetype": "",
         "name": "",
        }

        self.test_offices_not_isalpha = {
         "officetype": "@#$%^&*@!98ty",
         "name": "KANU",
        }

    def test_political_offices_valid(self):
        register = self.client.post('/offices',
                                    data=self.test_political_offices_valid,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 201)

    def test_political_offices_taken_inputs(self):
        register = self.client.post('/offices',
                                    data=self.test_offices_taken_inputs,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 409)

    def test_political_offices_empty_fields(self):
        register = self.client.post('/offices',
                                    data=self.test_offices_empty_fields,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_political_offices_not_isalpha(self):
        register = self.client.post('/offices',
                                    data=self.test_offices_not_isalpha,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)
