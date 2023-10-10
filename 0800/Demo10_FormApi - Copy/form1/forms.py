from django import forms


class StuRegistrationFrmApi(forms.Form):
    # fname = forms.CharField(initial="Sohan", max_length=20, min_length=2)
    # lname = forms.CharField(initial="Singh")
    # email = forms.EmailField()

    fname = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    roll = forms.CharField(widget=forms.HiddenInput)
    city = forms.CharField(widget=forms.Select(choices=[("d", "Delhi"), ("m", "Mumbai")]))
    Multicity = forms.CharField(widget=forms.SelectMultiple(choices=[("d", "Delhi"), ("m", "Mumbai"), ("g", "Goa"), ("a", "America"), ("l", "Los Angles")]))
    quali = forms.CharField(widget=forms.CheckboxInput)
    # Email = forms.EmailField()
