from django.conf.urls.defaults import patterns, include, url
#from django.views.generic.list_details import object_list
#from django.views.generic.create_update import create_object
#from abiturient.abit.models import AbitRequest
#from abiturient.abit.views import RequestList
from abit.views import AddAbitView

urlpatterns = patterns('abiturient.abit.views',
	url(r'^$', 'RequestList'),
	url(r'^add/$', AddAbitView.as_view()),
	url(r'^success/$', 'AddSuccess'),
	url(r'^init/$', 'Init'),
	#url(r'^$', object_list, {'queryset': AbitRequest.objects.all()}, name='list_abits'),
#	url(r'^add/$', create_object, {'model': AbitRequest}, name='add_abit'),
)