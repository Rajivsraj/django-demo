from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["first_name", "username", "email", "is_superuser", "is_staff"]


class UpdateUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["first_name", "last_name", "is_superuser", "is_staff", "is_active"]
