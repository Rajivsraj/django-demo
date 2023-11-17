from django.shortcuts import render
from .models import Register
from .forms import RegistrationForm


# Create your views here.
def user_registration(request):
    frm = RegistrationForm()

    if request.method == "POST":
        frm = RegistrationForm(request.POST)
        print(frm)
        print(request)
        if frm.is_valid():
            print("data valid")
        else:
            print("data not valid")

    return render(request, "register.html", {"form": frm})