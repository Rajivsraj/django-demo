from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.hashers import check_password, make_password

# b = check_password("123", "pbkdf2_sha256$390000$uZN07exAwEhBhcIOzdgMsW$TYaK8jB9h/ryCZbyJAsPcA4LPM3+NzCT2ZniKnSPYYo=")
# p = make_password("123")
# print(b)
# Create your views here.
def user_login(request):
    if request.session.get("username"):
        return redirect("dashboard")
    login_frm = LoginForm()
    if request.method == "POST":
        login_frm = LoginForm(data=request.POST)

        if login_frm.is_valid():
            username = login_frm.cleaned_data.get("username")
            password = login_frm.cleaned_data.get("password")
            # password = check_password(password,)
            usr = User.objects.get(username=username)
            pswd = usr.password

            if usr.username == username and check_password(password, pswd):
                request.session["username"] = username
                request.session["loggedin_status"] = True
                return redirect("dashboard")

    return render(request, "signalApp/login.html", context={"login_frm": login_frm})


def dashboard(request):
    username = request.session.get("username")
    ses_keys = request.session.keys()
    ses_values = request.session.values()
    return render(request, "signalApp/dashboard.html", context={"username": username, "ses_keys": ses_keys, "ses_values": ses_values})
