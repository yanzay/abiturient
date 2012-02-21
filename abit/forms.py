# coding=utf-8

from django import forms
from django.forms.widgets import DateInput
from abiturient.abit.models import AbitRequest

class AbitRequestForm(forms.ModelForm):
    class Meta:
        model = AbitRequest
        exclude = ('creator',)
        widgets = {'birth_date':DateInput(attrs={"class":"date"}),
                   'passport_date':DateInput(attrs={"class":"date"}),
                   'att_date':DateInput(attrs={"class":"date"}),
                   }
