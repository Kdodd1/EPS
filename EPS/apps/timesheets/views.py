from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "Login"
	return HttpResponse(response)