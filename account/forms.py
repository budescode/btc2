from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, CharField
from django.contrib.auth.hashers import make_password,is_password_usable,check_password
import string
import random 
from django.forms import BaseModelFormSet
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import MinimumLengthValidator, validate_password, password_validators_help_text_html
from django.shortcuts import render,redirect
from datetime import *
from django.http import HttpResponseRedirect, HttpResponse,QueryDict
from .models import PasswordResetEmail, ChangePassword, ChangePasswordCode, CreateProfie

class SignupForm(ModelForm):
    # Whoever coded this register activate used the inherit USER model
    # And this account for slight flexibility
    verify_password = forms.CharField(label="Type your password to verify ",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','password','verify_password','email']
        widgets = {
            'password':forms.PasswordInput(),
        }
    def clean(self):
        #rewriting clean method to check whether passwords match or not
        cleaned_data=super(SignupForm,self).clean()
        username=cleaned_data.get('username')
        email=cleaned_data.get('email')
        ps1=cleaned_data.get('password')
        ps2=cleaned_data.get('verify_password')
        # if email=="":
        #   self.add_error('email',"Please input your email!")
        if ps1!=ps2:
            msg="Password does not match!"
            self.add_error('verify_password',msg)
        # Save hashed password instead of password directly
        encoded_password=make_password(ps1,make_salt())
        cleaned_data['password']=encoded_password
        # Make sure email is unique
        if email and User.objects.filter(email=email).exclude(username=username).count():
            msg=""
            self.add_error('email',msg)
        # Validate password
        if ps1:
            try:
                validate_password(ps1,user=self)
                cleaned_data['help_text']=None
            except ValidationError:
                cleaned_data['help_text']=password_validators_help_text_html()
                self.add_error('password','Your password it too weak. Please choose another password')
        return cleaned_data



def make_salt():
    ###Your code here
    letters=string.ascii_letters
    result=random.sample(letters,5)
    return ''.join(result)





	
class RegisterForm(forms.Form):
    username = forms.CharField()
    

    first_name = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    phone_number = forms.IntegerField()
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( 
        attrs={'class':'form-control', 'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput( 
        attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password :
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid Log in details. Try Again....")
            if not user.is_active:
                raise forms.ValidationError("This User is no longer active.")
            return super(LoginForm, self).clean(*args, **kwargs)
    # username = forms.CharField(label='Email')
    # password = forms.CharField(widget=forms.PasswordInput)


# class SigninForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput( 
#         attrs={'class':'form-control', 'placeholder':'Enter username'}))
#     password = forms.CharField(widget=forms.PasswordInput( 
#         attrs={'class':'form-control', 'placeholder':'Enter Password'}))

#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#         if username and password :
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("Invalid Log in details. Try Again....")
#             if not user.is_active:
#                 raise forms.ValidationError("This User is no longer active.")
#             return super(SigninForm, self).clean(*args, **kwargs)



class EmailPasswordReset(forms.ModelForm):
    class Meta:
        model = PasswordResetEmail
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(),
        }


class ChangePasswordCodeForm(forms.ModelForm):
    class Meta:
        model = ChangePasswordCode
        fields = ['user_email']
        widgets = {
                    'user_email': forms.EmailInput(),
        }

class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = ChangePassword
        fields = ['new_password', 'confirm_new_password']
        widgets = {
                    'new_password':forms.PasswordInput(),
                    'confirm_new_password':forms.PasswordInput(),
        }
class CreateProfieForm1(forms.ModelForm):
    class Meta:
        model = CreateProfie 
        fields = ['first_name', 'last_name', 'phone_number']



