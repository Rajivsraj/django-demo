from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.
def user_registration(request):
    if request.method == "POST":
        frm = UserRegistrationForm(request.POST)
        if frm.is_valid():
            print(frm.cleaned_data)
            username = frm.cleaned_data.get("username")
            password = frm.cleaned_data.get("password1")
            fname = frm.cleaned_data.get("first_name")
            email = frm.cleaned_data.get("email")
            User(username=username, password=password, first_name=fname, email=email).save()
            messages.success(request, "User Registered Successfully")
            frm = UserRegistrationForm()
            redirect("user_registrations")
    else:
        frm = UserRegistrationForm()

    return render(request, "core/registration.html", context={"form": frm})
