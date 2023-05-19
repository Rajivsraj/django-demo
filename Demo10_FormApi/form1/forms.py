from django import forms


class StuRegistrationFrmApi(forms.Form):
    fname = forms.CharField(initial="Sohan", max_length=20, min_length=2)

    lname =forms.CharField(initial="Singh")
    email = forms.EmailField()
