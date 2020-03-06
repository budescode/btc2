from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
# from mysite.core import views as core_views
app_name='administrator'
urlpatterns = [
    path('', views.administrator, name="administrator" ),
	path('contact/', views.ContactView, name="contact" ),
	path('invest/', views.UserInvest, name="invest" ),
	path('email/', views.emailContact, name="email" ),
	path('deposit/', views.DepositView, name="deposit" ),
	path('depositnext/', views.DepositView2, name="depositnext" ),
	path('investment/', views.investmentView, name="investment" ),


]

