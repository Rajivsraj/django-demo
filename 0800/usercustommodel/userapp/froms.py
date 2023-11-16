from typing import Any
from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import AuthenticationForm
from . models import CustomUser

class Login_form(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' : 'True',
            'name' :  "email",
            'id' : "email",
            'class' : 'form-control',
            'placeholder' : "Email",
            'maxlength' : "50"
        })

        self.fields["password"].widget.attrs.update({
            'required': 'True',
            'name':  "password",
            'id': "password",
            'class': 'form-control',
            'placeholder': "password",
            'maxlength': "50"
        })

    class Meta:
        model = CustomUser
        fields = "__all__"
