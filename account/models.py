from django.db import models
from django.contrib.auth.models import User

import uuid
class PasswordResetEmail(models.Model):
	email = models.EmailField()
class ChangePasswordCode(models.Model):
	user_email = models.EmailField(max_length=50)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
class ChangePassword(models.Model):
	new_password = models.CharField(max_length=50, blank = False, null = False)
	confirm_new_password = models.CharField(max_length=50, blank = False, null = False)

class CreateProfie(models.Model):
	user = models.CharField(max_length=50, unique=True)
	email = models.EmailField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.IntegerField()
	amount = models.DecimalField(decimal_places = 2, default=0.00, max_digits=10000000000000000)
	date = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.first_name + ' ' + self.last_name

# models.CharField(max_length=50, unique=True)


class InvestmentModel(models.Model):
	choices = (
		('BASIC PACKAGE 30% DAILY', 'BASIC PACKAGE 30% DAILY'),
		('BUSINESS PACKAGE 15% DAILY', 'BUSINESS PACKAGE 15% DAILY'),
		('PROFESSIONAL PACKAGE 20% DAILY', 'PROFESSIONAL PACKAGE 20% DAILY'),

		)
	user_name = models.ForeignKey(User, on_delete = models.CASCADE)
	package = models.CharField(max_length=1000, choices=choices)
	amount = models.DecimalField(decimal_places = 2, default=0.00, max_digits=10000000000000000)
	date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)
	percentagerate = models.IntegerField()

	def __str__(self):
		return self.user_name.username