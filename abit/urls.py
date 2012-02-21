# coding=utf-8

from django.conf.urls.defaults import patterns, url
from django.views.generic.base import RedirectView
from abit.views import AddAbitRequestView, AbitRequestListView

urlpatterns = patterns('abiturient.abit.views',
    url(r'^$', RedirectView.as_view(url='list/')),
    url(r'^add/$', AddAbitRequestView.as_view()),
    url(r'^list/$', AbitRequestListView.as_view()),
#    url(r'^success/$', 'AddSuccess'),
    url(r'^init/$', 'Init'),
)