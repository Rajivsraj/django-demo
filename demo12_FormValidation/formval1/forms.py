from django import forms
from django.core.exceptions import ValidationError
import re

class RegFormCls(forms.Form):
    # name = forms.CharField(min_length=3, error_messages={"min_length":"required > 3 char"}) // inline validation
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 4:
            raise ValidationError("Needed > 3 char length in name")
        elif re.findall("\d", name):
            raise ValidationError("Only Chars required")


    def clean_username(self):
        usrnm = self.cleaned_data["username"]

        if len(usrnm) < 8:
            raise ValidationError("Required at least 8 Chars")
