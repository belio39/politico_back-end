import unittest
import json
from app import app
from io import BytesIO
from app.API.v1.views.political_party import *


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.test_political_party_valid = {
          "name": "belio",
          "headquateraddress": "dennis",
          "logo": (BytesIO(b'file content'), "test.png"),
        }

        self.test_party_taken_inputs = {
          "name": "deni",
          "headquateraddress": "kenya",
          "logo_url": "logo_url",
        }

        self.test_party_with_no_name = {
            "name": "",
            "headquateraddress": "dennis",
            "logo": "rotich",
        }

        self.test_with_no_hq_address = {
            "name": "belio",
            "headquateraddress": "",
            "logo": "rotich",
        }

        self.test_with_no_logo_url = {
            "name": "belio",
            "headquateraddress": "dennis",
            "logo": "",
        }
        self.test_with_missing_fields = {
            "name": "",
            "headquateraddress": "",
            "logo": "",
        }

        self.test_party_with_missing_fields = {
            "name": "",
            "headquateraddress": "",
            "logo": "",
        }

        self.test_patch_political_party_with_valid_fields = {
            "name": "belio",
            "headquateraddress": "dennis",
            "logo": (BytesIO(b'file content'), "test.png"),
        }

    def test_political_party_taken_inputs(self):
        register = self.client.post('/party',
                                    data=self.test_party_taken_inputs,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_political_party_valid(self):
        register = self.client.post('/party',
                                    data=self.test_political_party_valid,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 201)

    def test_political_party_with_no_name(self):
        register = self.client.post('/party',
                                    data=self.test_party_with_no_name,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_post_political_party_with_missing_fields(self):
        register = self.client.post('/party',
                                    data=self.test_party_with_missing_fields,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_patch_political_party_with_missing_fields(self):
        register = self.client.patch('/party/1',
                                     data=self.test_with_missing_fields,
                                     content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_political_party_with_no_hq_address(self):
        register = self.client.post('/party',
                                    data=self.test_with_no_hq_address,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_political_party_with_no_logo(self):
        register = self.client.post('/party',
                                    data=self.test_with_no_logo_url,
                                    content_type='multipart/form-data')
        self.assertEqual(register.status_code, 400)

    def test_delete_political_party_with_missing_fields(self):
        register = self.client.delete('/party/8')
        self.assertEqual(register.status_code, 404)

    def test_get_single_political_party(self):
        response = self.client.get('/party/1')
        self.assertEqual(response.status_code, 200)

    def test_get_all_political_party(self):
        response = self.client.get('/party')
        self.assertEqual(response.status_code, 200)

    def test_delete_political_party_not_found(self):
        response = self.client.delete('/politics/9')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):

        self.app = None
