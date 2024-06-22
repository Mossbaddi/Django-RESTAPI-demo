from django.shortcuts import render
from . import views
def index(request):
    return render(request, 'events_frontend/index.html')


def test(request):
	return render(request, 'events_frontend/test.html')