from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime
from account.models import InvestmentModel, CreateProfie
from dateutil.relativedelta import relativedelta



@login_required(login_url='/account/login/')
def home(request):
	return render(request, 'Administrator/index1.html')


@login_required(login_url='/account/login/')
def ContactView(request):
	return render(request, 'Administrator/contact.html')


@login_required(login_url='/account/login/')
def DepositView(request):
	return render(request, 'Administrator/deposit.html')


@login_required(login_url='/account/login/')
def DepositView2(request):
	package = request.POST.get('package')
	print(package)
	if package == 'BASIC PACKAGE 30% DAILY':
		qs = 'BASIC PACKAGE 30% DAILY'
		price = '$250.00 - $999.00'
		profit = '$140.00'
	elif package == 'BUSINESS PACKAGE 15% DAILY':
		qs = 'BUSINESS PACKAGE 15% DAILY'
		price = '$1000.00 - $9999.00'
		profit = '$210.00'
	elif package == 'PROFESSIONAL PACKAGE 20% DAILY':
		qs = 'PROFESSIONAL PACKAGE 20% DAILY'
		price = '$10000.00 - $50000.00'
		profit = '$350.00'
	return render(request, 'Administrator/deposit2.html', {'package':package, 'qs':qs, 'price':price,  'profit':profit})

@login_required(login_url='/account/login/')
def UserInvest(request):
	package=request.POST.get('package')
	amount=request.POST.get('amount')
	plan=request.POST.get('plan')
	rate = 0
	if package =='BASIC PACKAGE 30% DAILY':
		rate = 30
	elif package == 'BUSINESS PACKAGE 15% DAILY':
		rate = 15
	elif package == 'PROFESSIONAL PACKAGE 20% DAILY':
		rate = 20
	print(amount)
	InvestmentModel.objects.create(user_name=request.user, package=package, amount=amount, active=False, percentagerate=rate)
	return render(request, 'Administrator/invest.html', {'package':package, 'amount':amount, 'plan':plan})



def emailContact(request):
    messages.success(request, "Email Successfully sent, we'll respond shortly")
    return redirect('administrator:contact')
# Create your views here.
@login_required(login_url='/account/login/')
def administrator(request):
	try:
		qs1 = InvestmentModel.objects.filter(user_name=request.user, active=True).all().order_by('-date')[0]
		qs = CreateProfie.objects.get(user=request.user.username)
		amount = qs1.amount
		#print('normal amount', qs.amount)
		ago = qs1.date.date()
		now = datetime.now()
		date_format = "%Y-%m-%d"
		a = datetime.strptime(str(datetime.now().date()), date_format)
		b = datetime.strptime(str(ago), date_format)
		delta = a - b
		name = str(delta)
		value = str(delta).find(' day')
		value1 = name[0:value]
		rate = qs1.percentagerate
		calc = (15/100)*int(amount)
		#print (amount, calc)
		if qs1.date.date() == datetime.now().date():
			result='nothing'
		else:
			qs.amount = float(qs.amount) + float(calc)
			qs.save()
			qs1.date = datetime.now()
			qs1.save()
			print(qs1.date.date())
	except IndexError:
		qs = CreateProfie.objects.get(user=request.user.username)

# 	print('new amount', qs.amount, qs1.date.date())
	# diff = relativedelta(qs1.date, datetime.now())
	# delta = datetime.now().date() - ago
	# print (delta.days)
	# print(ago, now)

	return render(request, 'Administrator/index.html', {'qs':qs})



def investmentView(request):
	qs = InvestmentModel.objects.filter(user_name=request.user, active=True)
	return render(request, 'Administrator/investment.html', {'qs':qs})

