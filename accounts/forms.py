from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import query
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'password1', 'password2']


class contactusForm(ModelForm):
    class Meta:
        model = contactus
        fields = '__all__'