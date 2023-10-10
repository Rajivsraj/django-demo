from django import forms
from django.core import validators
from django.core.validators import ValidationError


def max_len_val(value):
    if len(value) < 2:
        raise ValidationError("Name Must be > 2 chars")


class FormVal(forms.Form):
    fname = forms.CharField(validators=[max_len_val])
    # fname = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    lname = forms.CharField(validators=[validators.MinLengthValidator(3)])
    marks = forms.IntegerField(validators=[validators.MinValueValidator(40), validators.MaxValueValidator(100)])