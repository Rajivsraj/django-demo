from django.shortcuts import render
from .forms import StuRegFormApi


# Create your views here.
def stuRegForm(request):
    frm = StuRegFormApi()
    return render(request, "app1/stuRegistraion.html", {"form": frm})
