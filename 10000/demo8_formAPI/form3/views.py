from django.shortcuts import render
from .forms import RegistrationForm


# Create your views here.
def register(request):
    frm = RegistrationForm(request.GET)
    username = request.GET.get("username")

    print(username)
    return render(request, "form3.html", context={"frm": frm})


