from django import forms
from django.core import validators

# def start_with_r(val):
#     if val[0] != "s":
#         raise forms.ValidationError("Username must be start from S char")

# def maxlen_err(val):
#     if len(val) <= 2:
#         raise forms.ValidationError("Len must be > 2")

class RegistrationForm(forms.Form):
    # username = forms.CharField(min_length=2)
    # username = forms.CharField()
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}), error_messages={"required": "This field is required custom", "max_length": "size exceed"})
    # username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}), validators=[start_with_r, maxlen_err])
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}), validators=[validators.int_list_validator(message="Enter Numbers only"), validators.MaxLengthValidator(10), validators.MinLengthValidator(10)])
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control form-control-sm"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-control-sm"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control form-control-sm"}))
