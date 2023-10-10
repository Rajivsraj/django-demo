from django import forms
from django.core.exceptions import ValidationError

# Validation
class StuReg(forms.Form):
    # name = forms.CharField(required=False, label="Your Name", max_length=10, strip=True, error_messages={"strip": "cant be space", "min_length": "Required at least 2 chars", "empty_value": "cant be empty"})
    name = forms.CharField(strip=False, error_messages={"strip": "cant be space"}, widget=forms.TextInput)
    lname = forms.CharField()
    email = forms.EmailField()

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) <4:
            raise ValidationError("required > 4 char")
        return data

# Normal
# class StuReg(forms.Form):
#     # name = forms.CharField(required=False, label="Your Name", max_length=10, strip=True, error_messages={"strip": "cant be space", "min_length": "Required at least 2 chars", "empty_value": "cant be empty"})
#     name = forms.CharField(strip=False, error_messages={"strip": "cant be space"}, widget=forms.TextInput)
#     consent = forms.BooleanField(error_messages={"required": "sdjklhjklsd"})
#     status = forms.CharField(widget=forms.CheckboxInput)
#     date = forms.DateField(input_formats=["%m/%d/%Y"])