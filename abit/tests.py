# coding=utf-8
from abit.models import AbitRequest, EducationalForm, Speciality, TestSubject
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
    def test_request_unicode(self):
        req = any_model(AbitRequest,surname=u'Pupkin',name=u'Vasiliy',father=u'Vitalievich')
        self.assertEqual(req.__unicode__(), u'Pupkin Vasiliy Vitalievich')
    def test_educational_form_unicode(self):
        form = any_model(EducationalForm,name=u'Заочная')
        self.assertEqual(form.__unicode__(),u'Заочная')
    def test_speciality_unicode(self):
        spec = any_model(Speciality,name=u'Информатика')
        self.assertEqual(spec.__unicode__(),u'Информатика')
    def test_subject_unicode(self):
        subj = any_model(TestSubject,name=u'Математика')
        self.assertEqual(subj.__unicode__(),u'Математика')


#class AbitRequestTest(TestCase):
#    def setUp(self):
#        self.abitreq = any_model()