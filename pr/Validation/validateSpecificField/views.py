from django.shortcuts import render
from .forms import RegFormCls, RegFromCls2


# Create your views here.
def regForm(request):
    frm = RegFormCls()

    if request.method == "POST":
        frm = RegFormCls(request.POST)

        if frm.is_valid():
            print("username: ", frm.cleaned_data["username"])
            print("Email: ", frm.cleaned_data["email"])
            print("Password: ", frm.cleaned_data["password"])

    return render(request, "formValidation/reg.html", {"frm": frm})


def regForm2(request):
    frm2 = RegFromCls2()

    if request.method == "POST":
        frm2 = RegFromCls2(request.POST)
    return render(request, "formValidation/reg2.html", {"frm2": frm2})