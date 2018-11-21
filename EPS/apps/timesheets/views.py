from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages
import bcrypt

def index(request):

	return render(request, "timesheets/index.html")

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.add_message(request, messages.ERROR, value, extra_tags='register')
		return redirect('/')
	else:
		password = request.POST['password']
		password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		user = User.objects.create(first_name= request.POST['first_name'], last_name = request.POST['last_name'], email= request.POST['email'], password= password)
		if user == User.objects.first():
			print(user)
			user.user_level = 9
			user.save()
			print(user.user_level)

			request.session['email'] = request.POST['email']
			request.session['user_id'] = user.id 
			return redirect('/adminDash')
		else:
			request.session['email'] = request.POST['email']
			request.session['user_id'] = user.id 
			return redirect('/userDash')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.add_message(request, messages.ERROR, value, extra_tags= "login")
		return redirect('/')
	else:
		request.session['email'] = request.POST['logemail']
		request.session['user_id'] = User.objects.get(email= request.POST['logemail']).id 
		if User.objects.get(email= request.POST['logemail']).user_level == 9:
			return redirect('/adminDash')
		else: 
			return redirect('/userDash')

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

def toReport(request):
    return redirect('/reports')
    #will require user id 

def toDash(request):
	return redirect('/adminDash')
	#will have if statement depending on the user level