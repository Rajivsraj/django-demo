from django import forms
from .models import Register, Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        # fields = "__all__"
        exclude = ["city"]


class TeacherForm(StudentForm):
    qualification = forms.CharField()
    teacher_name = forms.CharField(max_length=13)
    class Meta(StudentForm.Meta):
        # fields = ["teacher_name", "qualification", "username", "phone"]
        fields = "__all__"
        exclude = ["first_name"]




# class RegistrationForm(forms.Form):
#     ame = forms.CharField()
#     username = forms.CharField()
#     phone = forms.CharField()
#     password = forms.CharField()


class RegistrationForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name"}))
    class Meta:
        model = Register
        fields = ("first_name", "username", "phone", "password")
        labels = {
            "name": "Your Full Name",
            "username": "Enter username"
        }
        error_messages = {
            "name": {"required": "Please enter your name"},
            "username": {"required": "Username needed"}
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"required": True, "class": "form-control", "placeholder": "First Name"})
        }
        help_texts = {
            "first_name": "Enter your first name",
            "username": "usernamemememeemem"
        }


