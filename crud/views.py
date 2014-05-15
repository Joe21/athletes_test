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
	# Find the athlete from the db using the id passed with the request
	athlete = Athlete.objects.get(pk=athlete_id)
	template = loader.get_template('crud/detail.html')
	context = RequestContext(request, {
		'athlete' : athlete,
		})
	return HttpResponse(template.render(context))

def add(request):
	new_athlete = Athlete()
	template = loader.get_template('crud/add.html')
	context = RequestContext(request, {
		'new_athlete' : new_athlete,
		})
	return HttpResponse(template.render(context))