from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 
from django.forms import ModelForm
from django.db import models


class customform_models(models.Model):
    username = models.CharField(max_length=30 , null=True)
    password = models.CharField(max_length=30 , null=True)

class customlogin_form(ModelForm):
    class Meta:
        model = customform_models
        fields = ["username" , "password"]

class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'email', 'username']


class User_profile(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "is_staff",
                  "is_superuser", "is_active", "email", "date_joined"]
