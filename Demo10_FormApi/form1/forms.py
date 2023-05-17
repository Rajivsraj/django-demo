from django import forms


class StuRegistrationFrmApi(forms.Form):
    stuName = forms.CharField(initial="Sohan")
    lname =forms.CharField(initial="Singh")
    email = forms.EmailField()
