from django.http import HttpResponse
from django.template import RequestContext, loader

from crud.models import Athlete

def index(request):
	all_athletes = Athlete.objects.all()
	template = loader.get_template('crud/index.html')
	context = RequestContext(request, {
		'all_athletes' : all_athletes,
		})
	return HttpResponse(template.render(context))

def detail(request, athlete_id):
	return HttpResponse("Welcome to the detail page")

def add(request):
	return HttpResponse("Welcome to the add page")