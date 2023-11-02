from django import forms


# Built-in Form Fields
class RegistrationForm(forms.Form):
    username = forms.BooleanField()



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
