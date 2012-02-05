# coding=utf8

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from abiturient.abit.models import AbitRequest

class AbitRequestForm(forms.ModelForm):
    birth_date = forms.DateField(label='Дата рождения', widget=DateInput(attrs={"class":"date"}))
    passport_date = forms.DateField(label='Дата выдачи',widget=DateInput(attrs={"class":"date"}))
    att_date = forms.DateField(label='Дата выдачи аттестата',widget=DateInput(attrs={"class":"date"}))

    class Meta:
        model = AbitRequest
