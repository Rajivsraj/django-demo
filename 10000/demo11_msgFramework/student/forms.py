from django import forms
# from .models import Student
from django.contrib.auth.models import User


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ["first_name", "username", "email", "password"]