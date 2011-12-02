from django import forms
from abiturient.abit.models import Abiturient, AbitRequest, TestResult

class AbitForm(forms.ModelForm):
	class Meta:
		model = Abiturient
		
class AbitRequestForm(forms.ModelForm):
	class Meta:
		model = AbitRequest
		
class TestResultForm(forms.ModelForm):
	class Meta:
		model = TestResult
		exclude = ('abit', 'request')