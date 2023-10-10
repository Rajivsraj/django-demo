from django import forms


class RegForm(forms.Form):
    name = forms.CharField(initial="Rahul", help_text="this is name field", label_suffix="=>")
    email = forms.EmailField()
    psw = forms.CharField(widget=forms.PasswordInput())
    id = forms.CharField(widget=forms.HiddenInput())

