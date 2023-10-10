from django import forms

class StuRegFormApi(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
