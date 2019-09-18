from django.urls import path
from . import views

urlpatterns = [
	path(r'^weather/', views.index, name='weather'),
]