from django import forms
from django.core.exceptions import ValidationError


# Validation on a specific field
class RegFormCls(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        user = self.cleaned_data["username"]

        if len(user) <= 3:
            raise forms.ValidationError("Enter >3 chars")
        return user


class RegFromCls2(forms.Form):
    user = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        username = self.cleaned_data.get("user")

        if len(username) <= 3:
            raise forms.ValidationError("Invalid username")