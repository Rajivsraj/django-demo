from django.shortcuts import render
from .forms import RegForm


# Create your views here.
def reg_form(request):
    frm = RegForm()

    if request.method == "POST":
        frm = RegForm()

    return render(request, "reg.html", {"form": frm})