from django.forms import ModelForm
from abiturient.abit.models import AbitRequest

class AbitRequestForm(ModelForm):
    class Meta:
        model = AbitRequest

#class TestResultForm(forms.ModelForm):
#    class Meta:
#        model = TestResult
#        exclude = ('abit', 'request')