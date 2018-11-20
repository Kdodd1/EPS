from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^adminDash$', views.adminDash),
	url(r'^userDash$', views.userDash),
	url(r'^dailyReports$', views.dailyReports),
	url(r'^manage$', views.manage),
	url(r'^reports$', views.reports),
	url(r'^settings$', views.settings),
]