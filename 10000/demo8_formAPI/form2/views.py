from django.shortcuts import render
from .forms import RegistrationForm


# Create your views here.
def register_frm_api(request):
    frm = RegistrationForm()
    return render(request, "frm1.html", context={"form": frm})
