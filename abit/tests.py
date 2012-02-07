# coding=utf-8
from abit.models import AbitRequest

from django.test.client import Client
from django.test.testcases import TestCase
from django_any import any_model
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

class ModelsTest(TestCase):
    def test_request_model_unicode(self):
        req = any_model(AbitRequest,surname="Pupkin",name="Vasiliy",father="Vitalievich")
        self.assertEqual(req.__unicode__(), "Pupkin Vasiliy Vitalievich")


#class AbitRequestTest(TestCase):
#    def setUp(self):
#        self.abitreq = any_model()