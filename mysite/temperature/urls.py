from django.urls import path
from . import views

urlpatterns = [
	path(r'^temperature/temperature', views.index, name='temperature'), 
]