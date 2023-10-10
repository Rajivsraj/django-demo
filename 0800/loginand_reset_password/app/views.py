from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from .forms import CustomSignupForm , User_profile


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
            return redirect(request, "login")
        else:
            messages.error(request, "user Cant be added")
    return render(request, "registration/signup.html", context={"frm": frm})


def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, "You  are alreday logged in")
        return redirect("dashboard")
    else:
        frm = AuthenticationForm()
        if request.method == "POST":
            frm = AuthenticationForm(request = None, data = request.POST)
            if frm.is_valid():
                username = frm.cleaned_data.get("username")
                password = frm.cleaned_data.get("password")
            #    login(request, request.user) without authenticate function
                usr = authenticate(username = username, password = password)
                if usr is not None:
                    login(request, usr)
            # return HttpResponseRedirect("/admin/")
                    messages.success(request, "Successfully Loged in")
                    return redirect("dashboard")
    return render(request, "registration/login.html", context={"frm":frm})



def user_logout(request):
    logout(request)
    return redirect("login")

def reset_password(request):
    frm = PasswordChangeForm(request.user)
    if request.method == "POST":
        frm = PasswordChangeForm(request.user, request.POST)
        if frm.is_valid():
            frm.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Passwor changed sucessfully")
            return redirect("login")
    return render(request, "registration/re_pass.html", context={"frm" : frm})

def user_profile(request):
    frm = User_profile(instance = request.user)
    if request.method == "POST":
        frm = User_profile(request.POST, instance = request.user)
        if frm.is_valid():
            frm.save()
            messages.success(request, "Profile Updated Sucessfully")
    return render(request, "registration/profile.html", context={"form": frm})


def dashboard(request):
    if request.user.is_authenticated:     # This is for the validation of user can only go to dashboard when he is logged in otherwise else part will run
        messages.success(request, "Welcome")
        frm = User_profile(request.POST, instance=request.user)
        old_data = User_profile(request.user)
        return render(request, "registration/dashboard.html", context={"name": request.user.first_name, "old_data" : old_data ,  "frm": request.user})
    else:
        return redirect("login")


