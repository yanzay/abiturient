# coding=utf-8
from django.db.models.query import QuerySet
from django.db.models.sql.query import Query
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render_to_response, redirect
from django.views.generic.list import ListView
from abit.forms import AbitRequestForm
from abit.models import AbitRequest, EducationalForm, Speciality
from abit.dummy import Generator

class AddAbitRequestView(CreateView):
    model = AbitRequest
    template_name = 'abitrequest_form.html'
    context_object_name = 'abit_form'
    form_class = AbitRequestForm
    success_url = '/abit/list/'

    def form_valid(self, form):
        inst = form.save(commit=False)
        inst.creator = self.request.user
        inst.save()
        return redirect(self.success_url)

class AbitRequestListView(ListView):
#    model = AbitRequest
    template_name = 'reqslist.html'
    context_object_name = 'abitrequest_list'
    paginate_by = 50

    def get_queryset(self):
        return AbitRequest.objects.all().order_by('-date')

class EditAbitRequestView(UpdateView):
    model = AbitRequest
    template_name = 'abitrequest_form.html'
    context_object_name = 'abit_form'
    form_class = AbitRequestForm
    success_url = '/abit/list/'


def reqcmp(x,y):
    return -cmp(x.sum_bal,y.sum_bal)

class RatingListView(ListView):
    template_name = 'rating.html'
    context_object_name = 'abitrequest_list'

    def getSpec(self):
        if 'q' in self.request.GET:
            return self.request.GET['q']
        else:
            return u'Економіка підприємства'

    def get_queryset(self):
#        self.args[0]
        spec = self.getSpec()
        spec = Speciality.objects.filter(name=spec)
#        return HttpResponse(spec)
        reqs = list(AbitRequest.objects.all().filter(speciality=spec))
        reqs.sort(cmp=reqcmp)
        return reqs

    def get_context_data(self, **kwargs):
        context = super(RatingListView,self).get_context_data(**kwargs)
        context['specs'] = Speciality.objects.all()
        context['selected'] = self.getSpec()
        return context

def Init(request):
    g = Generator()
    g.generateBase()
    g.generateAbitRequests(request)
    return HttpResponseRedirect('/abit/list/')
