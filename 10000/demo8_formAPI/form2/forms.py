from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=10, min_length=3, required=False)
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
