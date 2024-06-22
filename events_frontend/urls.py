# events_frontend/urls.py
from django.urls import path
from . import views



app_name = 'events_frontend' # Pour définir un namespace

urlpatterns = [
    path('', views.index, name='home'),
	path('test/', views.test, name='test'),
	path('event_list/', views.event_list, name='event_list'),
	path('event_detail/<int:event_id>/', views.event_detail, name='event_detail'),
]
