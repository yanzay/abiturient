# coding=utf-8
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response, redirect
from django.views.generic.list import ListView
from abit.forms import AbitRequestForm
from abit.models import AbitRequest, EducationalForm
from abit.dummy import Generator

class AddAbitRequestView(CreateView):
    model = AbitRequest
    template_name = 'abitrequest_form.html'
    context_object_name = 'abit_form'
    form_class = AbitRequestForm
    success_url = '/abit/list'

class AbitRequestListView(ListView):
    model = AbitRequest
    template_name = 'reqslist.html'
    context_object_name = 'abitrequest_list'
    paginate_by = 50

def Init(request):
    g = Generator()
    g.generateBase()
    g.generateAbitRequests(request)
    return HttpResponseRedirect('/abit/list/')
