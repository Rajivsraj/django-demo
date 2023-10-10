from django import forms
from .models import StudentDetails, AddStaff


class StuDetailFrm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = ["name", "email", "password", "phone"]


class StaffForm(forms.ModelForm):
    class Meta:
        model = AddStaff
        fields = "__all__"
