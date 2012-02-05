from django.conf.urls.defaults import patterns, include, url
#from django.views.generic.list_details import object_list
#from django.views.generic.create_update import create_object
#from abiturient.abit.models import AbitRequest
#from abiturient.abit.views import RequestList
from django.views.generic.base import RedirectView
from abit.views import AddAbitRequestView, AbitRequestListView

urlpatterns = patterns('abiturient.abit.views',
    url(r'^$', RedirectView.as_view(url='list/')),
    url(r'^add/$', AddAbitRequestView.as_view()),
    url(r'^list/$', AbitRequestListView.as_view()),
    url(r'^success/$', 'AddSuccess'),
    url(r'^init/$', 'Init'),
)