# coding=utf-8

from django.conf.urls.defaults import patterns, url
from django.views.generic.base import RedirectView
from abit.views import AddAbitRequestView, AbitRequestListView, EditAbitRequestView

urlpatterns = patterns('abiturient.abit.views',
    url(r'^$', RedirectView.as_view(url='list')),
    url(r'^add/$', AddAbitRequestView.as_view()),
    url(r'^list/$', RedirectView.as_view(url='page1')),
    url(r'^list/page(?P<page>[0-9]+)/$', AbitRequestListView.as_view()),
#    url(r'^success/$', 'AddSuccess'),
    url(r'^init/$', 'Init'),
    url(r'^edit/(?P<pk>[0-9]+)/$', EditAbitRequestView.as_view())
)