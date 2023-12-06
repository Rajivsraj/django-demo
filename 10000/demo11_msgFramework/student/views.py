from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def student_reg(request):
    if request.method == "POST":
        frm = StudentRegistrationForm(request.POST)
        if frm.is_valid():
            fname = frm.cleaned_data.get("first_name")
            username = frm.cleaned_data.get("username")
            email = frm.cleaned_data.get("email")
            password = frm.cleaned_data.get("password")
            User(first_name=fname, username=username, email=email, password=password).save()
            # messages.add_message(request, messages.SUCCESS, "User Register Successfully")
            messages.success(request, "User Register Successfully")
            return redirect("user_registration")
        else:
            messages.add_message(request, messages.ERROR, "all fields are required")

    else:
        frm = StudentRegistrationForm()

    return render(request, "student/registration.html", context={"form": frm})