from django.shortcuts import render, redirect
from django import forms 
from django.contrib.auth.forms import AuthenticationForm  , UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def register(request):
    frm = UserCreationForm()
    # frm = CustomSignupForm()
    if request.method == "POST":
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request , "Register Succesfully")
            return redirect("Login")
        else:
            messages.error(request , "Can`t be Registered")
    return render(request , "register.html" , context={"frm" :frm})


def login_user(request):
    
    if request.user.is_authenticated:
        return redirect("dashboard")

    else:
        frm = AuthenticationForm() 
        if request.method == "POST":
            frm = AuthenticationForm(request=None, data=request.POST)
            if frm.is_valid():
                usrnm = frm.cleaned_data.get("username")
                passwo = frm.cleaned_data.get("password")
                print("au b")
                usr = authenticate(username=usrnm, password=passwo)
                print("au af")
                if usr is not None:
                    login(request, usr)

                    messages.add_message(request, messages.SUCCESS, "Loged in Succsessfully")
                    return redirect("dashboard")
    return render(request, "login.html", context={"frm": frm})


def logout_user(request):
    logout(request)
    return redirect("Login")


def dashboard(request):
    return render(request , "dashboard.html")
