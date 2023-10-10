from django import forms


class MyForm(forms.Form):
    YEAR_IN_SCHOOL_CHOICES = [
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]
    name = forms.CharField(label="First Name", min_length=5, help_text="Required 5 digits only")
    email = forms.EmailField()
    password = forms.CharField()
    city = forms.ChoiceField(choices=[("delhi", "Delhi")])