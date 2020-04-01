from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from urllib.parse import quote, quote_plus
from django.http import HttpResponseRedirect, HttpResponse
from urllib.parse import quote, quote_plus
from django.contrib.auth.decorators import login_required
import requests
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
from crypto_news_api import CryptoControlAPI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.core.mail import send_mail



api = CryptoControlAPI("ae09e411009fafddd814a7b142edc0a6")
proxyApi = CryptoControlAPI("ae09e411009fafddd814a7b142edc0a6", "http://cryptocontrol_proxy/api/v1/public")
a=0
total_list = []
def home(request):
    x = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = x.json()
    dollarrate = data['bpi']['USD']['rate']
    poundrate = data['bpi']['GBP']['rate']
    eurorate = data['bpi']['EUR']['rate']
    updated = data['time']['updated']
    disclaimer = data['disclaimer']
    news = api.getTopNewsByCoin("bitcoin")
    newslist = []
    for i in range(15):
        image = news[i]['originalImageUrl']
        title = news[i]['title']
        publishedAt = news[i]['publishedAt']
        newslist.append({'title':title, 'image':image, 'publishedAt':publishedAt})
    context = {'newslist':newslist, 'data':data ,'dollarrate':dollarrate, 'updated':updated, 'disclaimer':disclaimer, 'poundrate':poundrate, 'eurorate':eurorate}
    return render(request, 'home/index.html', context)


def about_view(request):
	return render(request, 'home/about.html')
def pricing_view(request):
	return render(request, 'home/pricing.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        to_email = ['solomonmorgan2848@gmail.com']
        body = request.POST.get('message')
        subject = "www.thebtcminers.com"
        from_email = settings.EMAIL_HOST_USER
        # Now we get the list of emails in a list form.
        #Opening a file in python, with closes the file when its done running
        with open(settings.BASE_DIR + "/templates/account/change_password_email.txt") as sign_up_email_txt_file:
        	sign_up_message = sign_up_email_txt_file.read()
        message = EmailMultiAlternatives(subject=subject, body=body,from_email=from_email, to=to_email )
        html_template = get_template("email_send.html").render({'name':'name', 'email':email, 'message':body})
        message.attach_alternative(html_template, "text/html")
        message.send()
        return render(request, 'contact_send.html')

    return render(request, 'contact.html')
