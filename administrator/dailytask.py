from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from index.models import Poster
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
import csv, io
from django.contrib import messages
from .models import CountryDetails, MyItems, Cart
from project.utils import render_to_pdf
from django.template.loader import get_template
from django.utils import timezone
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse ,QueryDict
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm, CategoryForm, ChangePasswordCodeForm, ChangePasswordForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import *

from .models import Profile, ChangePasswordCode
from django.shortcuts import get_list_or_404, get_object_or_404

import urllib
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


date = request.POST.get('date')
print(date)
qs = Cart.objects.filter(paid=True, date=str(date)).order_by('-date')
totalsales = 0
totalamount = 0

for i in qs:
	totalsales = totalsales+i.qty
	totalamount = totalamount+i.price