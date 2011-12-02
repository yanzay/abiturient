from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from abiturient.abit.forms import AbitForm, AbitRequestForm, TestResultForm
from abiturient.abit.factory import AbitFactory

from abit.models import *

def RequestList(request):
	reqs = AbitRequest.objects.all()
	context = RequestContext(request, {'reqs': reqs})
	return render_to_response('reqslist.html', context)
	
def AddAbit(request):
	if not request.POST:
		abform = AbitForm()
		resultform = TestResultForm()
	else:
		abitFactory = AbitFactory()
		abitFactory.addAbit(request.POST)
		return redirect(AddSuccess)
	return render_to_response('form.html',
		{'abit_form': abform, 'result_form': resultform},
		context_instance=RequestContext(request))

def AddSuccess(request):
	return render_to_response('success.html', {'link': request.META['HTTP_REFERER']})
	
def Init(request):
	# Init EducationalForm
	EducationalForm.objects.all().delete()
	edform1 = EducationalForm(name=u'Денна')
	edform2 = EducationalForm(name=u'Заочна')
	edform1.save()
	edform2.save()
	return redirect(RequestList)
	