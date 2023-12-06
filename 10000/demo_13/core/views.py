from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from .forms import UserRegistration, UpdateUserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash



def register(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        if request.method == "POST":
            frm = UserRegistration(request.POST)
            if frm.is_valid():
                print(frm.cleaned_data)
                fname = frm.cleaned_data.get("first_name")
                email = frm.cleaned_data.get("email")
                username = frm.cleaned_data.get("username")
                user = frm.save(commit=False)  # <---
                user.set_password(frm.cleaned_data.get('password1'))  # <---
                user.save()

                # User(username=username, password=password, first_name=fname, email=email).save()
                messages.success(request,"User Registered Successfully")
            return render(request, template_name="core/registration.html", context={"form": frm})
        else:
            frm = UserRegistration()
            return render(request, template_name="core/registration.html", context={"form": frm})


def user_login(request):

    if request.user.is_authenticated:
        return redirect("profile")
    else:
        if request.method == "POST":
            frm = AuthenticationForm(request=request, data=request.POST)
            print(frm)
            if frm.is_valid():
                username = frm.cleaned_data.get("username")
                password = frm.cleaned_data.get("password")
                usr = authenticate(username=username, password=password)
                if usr != None:
                    login(request, usr)
                    return redirect("profile")
            return render(request, template_name="core/login.html", context={"form": frm})
        else:
            frm = AuthenticationForm()
    return render(request, template_name="core/login.html", context={"form": frm})


def user_profile(request):
    if request.user.is_authenticated:
       return render(request, "core/profile.html", context={"name": request.user.first_name})
    else:
        return redirect("login")

def user_logout(request):
    logout(request)
    return redirect("login")


def change_user_password(request):
    if request.method == "POST":
        frm = PasswordChangeForm(user=request.user, data=request.POST)
        if frm.is_valid():
            print(frm.cleaned_data)
            frm.save()
            update_session_auth_hash(request, frm.user)
    else:
        print(request.user)
        frm = PasswordChangeForm(user=request.user)
        print(frm)
    return render(request, template_name="core/change-password.html", context={"form": frm})


def user_profile_change(request):
    if request.method == "POST":
        frm = UpdateUserProfileForm(request.POST, instance=request.user)
        if frm.is_valid():
            frm.save()
            return redirect("profile")
            # return render(request, template_name="core/change-profile.html", context={"form": frm})
    else:
        frm = UpdateUserProfileForm(instance=request.user)
        return render(request, template_name="core/change-profile.html", context={"form": frm})