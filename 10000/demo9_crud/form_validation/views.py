from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm
from .models import User


def home(request):
    return HttpResponse("<h1>Hi Home page</h1>")
# after form submission successfully data should not be shown into the field
# Create your views here.
def register(request):
    if request.method == "POST":
        frm = RegistrationForm(request.POST)
        if frm.is_valid():
            fname = frm.cleaned_data.get("first_name")
            username = frm.cleaned_data.get("username")
            phone = frm.cleaned_data.get("phone")
            email = frm.cleaned_data.get("email")
            password = frm.cleaned_data.get("password")
            usr = User(first_name=fname, username=username, phone=phone, email=email, password=password)
            usr.save()
            print("data saved")
            return HttpResponseRedirect("/register/")
        else:
            print("Invalid data")
    else:
        frm = RegistrationForm()

    return render(request, "validations/registration.html", context={"frm": frm})
