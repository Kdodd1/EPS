from django.shortcuts import render, HttpResponse, redirect

def index(request):

	return render(request, "timesheets/index.html")

def adminDash(request):

	return render(request,"timesheets/adminDash.html")