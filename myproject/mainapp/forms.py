from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'theme', 'message', 'status']


class CheckForm(forms.ModelForm):
    class Meta:
        model = ChekOut
        fields = ['name', 'username', 'password', 'company', 'email', 'title', 'first_name', 'middle_name', 'sity',
                  'street', 'zip_code', 'phone', 'mobil_phone', 'fax', 'about']  # 'country', 'regions'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'email', 'city', 'message']



# class BlogForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     city = forms.CharField(max_length=70)
#     message = forms.CharField(max_length=5000)
#
#     def