from django import forms
from .models import Register


# class RegistrationForm(forms.Form):
#     ame = forms.CharField()
#     username = forms.CharField()
#     phone = forms.CharField()
#     password = forms.CharField()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ("name", "username", "phone", "password")