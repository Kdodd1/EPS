from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^adminDash$', views.adminDash),
	url(r'^userDash$', views.userDash),
	url(r'^dailyReports$', views.dailyReports),
	url(r'^manage$', views.manage),
	url(r'^reports$', views.reports),
	url(r'^toReport$', views.toReport),
	url(r'^settings$', views.settings),
	url(r'^changeemail$', views.changeEmail),
	url(r'^changename$', views.changeName),
	url(r'^resetpassword$', views.resetPassword),
	url(r'^toDash$', views.toDash),
	url(r'^(?P<id>\d+)/delete$', views.delete),
    url(r'^(?P<id>\d+)/level$', views.level),
]