from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def registration(request):
    frm = UserCreationForm()
    if request.method == "POST":
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, "User Added Successfully")
        else:
            messages.error(request, "user Cant be added")
    return render(request, "registration/signup.html", context={"frm": frm})