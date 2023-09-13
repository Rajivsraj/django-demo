from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register(request):
    frm = UserCreationForm()
    if request.method == "POST":
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            request.session['username'] = request.user
            request.session['password'] = request.user.password
            request.session['email'] = request.user.email
            frm.save()
            messages.add_message(request ,messages.SUCCESS, "You are Registered Sucsessfully with us")
        else :
            messages.add_message(request, messages.ERROR ,"You were not registered")
    return render(request , "register/singup.html", context={"frm" : frm})








