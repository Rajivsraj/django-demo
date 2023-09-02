from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import login , logout , authenticate
from django . contrib import messages
from .forms import customlogin_form
from django . contrib .auth . models import User
# Create your views here.

def resgister(request):
    frm = UserCreationForm()
    if request.method == "POST":
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request , "Register Succesfully")
            return redirect("Login")
        else:
            messages.error(request , "Can`t be Registered")
    return render(request , "register.html" , context={"frm" :frm})


def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, "You  are alreday logged in")
        return redirect("dashboard")
    else:
        msg = {}
        frm = customlogin_form()
        if request.method == "POST":
            frm = customlogin_form(request.POST)
            if frm.is_valid():
                usern = frm.cleaned_data.get("username")
                passwor = frm.cleaned_data.get("password")
                # login(request , request.user) 
                # chechk = User.objects.filter(username = usern , password = passwor)
                usr = authenticate(username = usern , password = passwor)
                if usr is not None:
                    request.session["username"] = usr.username
                    request.session["password"] = usr.password

                    if request.session.get("username") == usr.username:
                        messages.success(request , "Logged in succesfully")
                        print("jdkfhgfgh")
                        return redirect("dashboard")
                    if request.session.get("username") != usr.username:
                        print("can`t")
                        return redirect("Login")
                    
    return render(request , "login.html" , context={"frm" : frm , "msg" :msg})

def dashboard(request):
        username = request.session.get("username")
        password = request.session.get("password")

        session = request.session
        return render(request , "dashboard.html" , context={"usrname" : username , "password" : password, "session" : session})

def user_logout(request):
    msg = {}
    del request.session["username"]
    # del request.session["password"]
    usrnm = request.session.get("username")
    msg["sucess"] = "Logout Secessfully"
    logout(request)
    return render(request , "logout.html" , context={"data":usrnm, "msg":msg})
