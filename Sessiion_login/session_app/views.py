from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import login , logout , authenticate
from django . contrib import messages
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
        frm = AuthenticationForm()
        if request.method == "POST":
            frm = AuthenticationForm(request = None , data = request.POST)
            if frm.is_valid():
                username = frm.cleaned_data.get("username")
                password = frm.cleaned_data.get("password")
                # login(request , request.user) 
                usr = authenticate(username = username , password = password)
                if usr is not None:
                    request.session["username"] = "Abhishek"
                    request.session["password"] = "google"
                    login(request, usr)
                    messages.success(request , "Logged in succesfully")
                    return redirect("Login")
    return render(request , "login.html" , context={"frm" : frm})

def dashboard(request):
    if request.user.is_authenticated:
        username = request.session.get("username")
        password = request.session.get("password")

        session = request.session
        return render(request , "dashboard.html" , context={"usrname" : username , "password" : password , "session" : session})
    else:
        return redirect("Login")
def user_logout(request):
    msg = {}
    del request.session["username"]
    del request.session["password"]
    usrnm = request.session.get("username")
    msg["sucess"] = "Logout Secessfully"
    logout(request)
    return render(request , "logout.html" , context={"data":usrnm, "msg":msg})
