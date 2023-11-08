from django import forms


# 04/11/2023
# validation
class RegistrationFormValidation(forms.Form):
    fullname = forms.CharField(min_length=2)
    username = forms.CharField(min_length=5)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)


# Built-in Form Fields
# class RegistrationForm(forms.Form):
#     username = forms.BooleanField()



# class RegistrationForm(forms.Form):
#     rollno = forms.CharField(disabled=True, initial=101)
#     fullname = forms.CharField(widget=forms.TextInput(attrs={
#         "Placeholder": "Full Name"
#     }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "form-control",
#         "id": "password",
#         "placeholder": "Password",
#         "mohan": "abc",
#     }))
#     username = forms.CharField()
#     email = forms.EmailField()



# Form field Arguments
# class RegistrationForm(forms.Form):
#     # rollno = forms.IntegerField(disabled=True, initial=101)
#     rollno = forms.CharField(disabled=True, initial=101)
#     # rollno = forms.CharField(widget=forms.HiddenInput)
#     # fullname = forms.CharField(required=False, label="Full Name", initial="Rajat Chaudhary", help_text="Please enter your full name")
#     fullname = forms.CharField(required=False, label="Full Name", help_text="Enter your name")
#     username = forms.CharField()
#     email = forms.EmailField()



# class RegistrationForm(forms.Form):
#     rollno = forms.CharField(widget=forms.HiddenInput)
#     fullname = forms.CharField()
#     username = forms.CharField()
#     email = forms.EmailField()
