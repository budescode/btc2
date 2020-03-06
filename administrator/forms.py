from django.contrib.auth.models import User
from django import forms
from .models import VendorPost
from ckeditor.widgets import CKEditorWidget




class VendorPostForm(forms.ModelForm):
	class Meta:
		model = VendorPost
		exclude = ['user']

	


