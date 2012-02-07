# coding=utf-8

from django.test.client import Client
from django.test.testcases import TestCase
#from functional_tests import FunctionalTest
#from selenium.selenium import
#from django.utils import unittest

class ResponseStatusTest(TestCase):
    def setUp(self):
        self.client = Client()
    def test_abit_add(self):
        self.assertEqual(self.client.get('/abit/add/').status_code,200)
    def test_abit_list(self):
        self.assertEqual(self.client.get('/abit/list/').status_code,200)
    def test_abit_main(self):
        self.assertEqual(self.client.get('/abit/').status_code,301)

#class AbitRequestTest(TestCase):
#    def setUp(self):
#        self.abitreq = any_model()