from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class CustomSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

class User_profile(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "is_staff", "is_superuser", "is_active", "email", "date_joined"]
