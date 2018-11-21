from django.db import models

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	password= models.CharField(max_length=255)
	user_level = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

class Report(models.Model):
	user = models.ForeignKey(User, related_name="reports")
	task = models.CharField(max_length=85)
	notes = models.TextField()
	assist = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Day(models.Model):
	clock_in = models.DateTimeField(auto_now_add=True)
	clock_out = models.DateTimeField()
	date = models.DateField(auto_now_add=True)
	report = models.OneToOneField(Report, related_name='day')
	user = models.ForeignKey(User, related_name="days")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)