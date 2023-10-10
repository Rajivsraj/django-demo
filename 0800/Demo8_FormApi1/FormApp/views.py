from django.shortcuts import render
from .forms import MyForm


# Create your views here.
def reg_form(request):
    frm = MyForm()
    return render(request, "formapp/registration.html", {"reg_form": frm})
