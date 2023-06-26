from django import forms
from django.core.exceptions import ValidationError
import re

class RegFormCls(forms.Form):
    # name = forms.CharField(min_length=3, error_messages={"min_length":"required > 3 char"}) // inline validation
    name = forms.CharField(initial="")
    username = forms.CharField(initial="")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name1 = cleaned_data.get("name")

        username = forms.CharField()

        if len(name1) <= 2:
            raise ValidationError("Enter >2 chars")
        else:
            self.name = cleaned_data["name"]

        if len(username) < 8:
            raise ValidationError("Enter at least 8 chars")
        else:
            self.username = cleaned_data["username"]
