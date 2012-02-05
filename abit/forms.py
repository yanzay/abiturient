from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from abiturient.abit.models import AbitRequest

class AbitRequestForm(forms.ModelForm):
    birth_date = forms.DateField(widget=DateInput(attrs={"class":"date"}))
    class Meta:
        model = AbitRequest

#class TestResultForm(forms.ModelForm):
#    class Meta:
#        model = TestResult
#        exclude = ('abit', 'request')