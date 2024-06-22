from django.shortcuts import render
from . import views
import requests
from django.conf import settings

def index(request):
    return render(request, 'events_frontend/index.html')


def test(request):
	return render(request, 'events_frontend/test.html')

def event_list(request):
	response = requests.get(f"{settings.API_URL}/events/")
	events = response.json()
	return render(request, 'events_frontend/event_list.html', {'events': events})

def event_detail(request, event_id):
	response = requests.get(f"{settings.API_URL}/events/{event_id}/")
	event = response.json()
	return render(request, 'events_frontend/event_detail.html', {'event': event})