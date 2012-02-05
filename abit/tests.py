from django.test.client import Client
from django.utils import unittest

class ResponseStatusTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    def test_abit_add(self):
        self.assertEqual(self.client.get('/abit/add/').status_code,200)
    def test_abit_list(self):
        self.assertEqual(self.client.get('/abit/list/').status_code,200)
    def test_abit_main(self):
        self.assertEqual(self.client.get('/abit/').status_code,301)