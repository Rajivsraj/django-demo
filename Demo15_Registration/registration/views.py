from django.shortcuts import render, redirect, HttpResponseRedirect
# AuthenticationForm is used for login form
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomSignupForm

# Create your views here.
def registration(request):
    # frm = UserCreationForm()
    frm = CustomSignupForm()
    if request.method == "POST":
        # frm = UserCreationForm(request.POST)
        frm = CustomSignupForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, "User Added Successfully")
        else:
            messages.error(request, "user Cant be added")
    return render(request, "registration/signup.html", context={"frm": frm})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        frm = AuthenticationForm()
        if request.method == "POST":
            frm = AuthenticationForm(request=None, data=request.POST)
            print(frm)
            if frm.is_valid():
                usrnm = frm.cleaned_data.get("username")
                password = frm.cleaned_data.get("password")
                usr = authenticate(username=usrnm, password=password)
                if usr is not None:
                    login(request, usr)     # session create
                    # return HttpResponseRedirect("/admin/")
                    messages.success(request, "You're successfully  logged in")
                    return redirect("dashboard")
        return render(request, "registration/login.html", context={"frm": frm})


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "registration/dashboard.html", {"name": request.user})
    else:
        return redirect("login")


def logut(request):
    logout(request)
    return redirect("login")


def resetPassword(request):
    frm = PasswordChangeForm(request.user)
    if request.method == "POST":
        frm = PasswordChangeForm(request.user, request.POST)
        if frm.is_valid():
            frm.save()
            update_session_auth_hash(request, frm.user)
    return render(request, "registration/reset-password.html", context={"form": frm})
