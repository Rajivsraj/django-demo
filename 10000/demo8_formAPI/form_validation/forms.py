from django import forms
from django.core import validators

def start_with_r(val):
    if val[0] != "s":
        raise forms.ValidationError("Username must be start from S char")

def maxlen_err(val):
    if len(val) <= 2:
        raise forms.ValidationError("Len must be > 2")

class RegistrationForm(forms.Form):
    # username = forms.CharField(min_length=2)
    # username = forms.CharField()
    username = forms.CharField(validators=[start_with_r, maxlen_err])
    phone = forms.CharField(validators=[validators.int_list_validator(message="Enter Numbers only"), validators.MaxLengthValidator(10), validators.MinLengthValidator(10)])
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if len(username) < 2:
    #         raise forms.ValidationError("Enter >2 chars")

class Form1(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()


# class Form1(forms.Form):
#     fname = forms.CharField()
#     lname = forms.CharField()
#     email = forms.EmailField()
#     phone = forms.CharField()

    # def clean_fname(self):
    #     fname = self.cleaned_data.get("fname")
    #     print(fname)
    #     # if len(fname) < 3:
    #     #     raise forms.ValidationError("Please fill >3 chars")
    #     # # print(fname)
    #     return "Mr. "+fname

    # def clean(self):
    #     cleaned_data = super().clean()
    #     fname = cleaned_data.get("fname");
    #     lname = cleaned_data.get("lname");
    #
    #     # It will give only one error msg for all the fields
    #     if len(fname) < 3:
    #         print(fname)
    #         raise forms.ValidationError("enter proper name")
    #
    #     if len(lname) < 3:
    #         # print(lname)
    #         raise forms.ValidationError("enter last name name")