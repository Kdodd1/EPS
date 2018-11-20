from django.shortcuts import render, HttpResponse, redirect

def index(request):

	return render(request, "timesheets/index.html")

def adminDash(request):

	return render(request,"timesheets/adminDash.html")

def userDash(request):
	return render(request, "timesheets/userDash.html")

def dailyReports(request):
	return render(request, "timesheets/dailyReports.html")

def manage(request):
	return render(request, "timesheets/manage.html")

def reports(request):
	return render(request, "timesheets/reports.html")

def settings(request):
	return render(request, "timesheets/settings.html")

