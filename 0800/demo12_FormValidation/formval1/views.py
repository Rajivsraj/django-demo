from django.shortcuts import render
from .forms import RegFormCls
from .forms2 import RegFormCls as regFrom2


# Create your views here.
def regFormFun(request):
    frm = RegFormCls()

    if request.method == "POST":
        frm = RegFormCls(request.POST)

        if frm.is_valid():
            name = frm.cleaned_data["name"]
            username = frm.cleaned_data["username"]
            email = frm.cleaned_data["email"]
            password = frm.cleaned_data["password"]

            print("name: ", name)
            print("name: ", username)
            print("name: ", email)
            print("name: ", password)
    return render(request, "formval1/registration.html", {"frm": frm})


def regFormFun2(request):
    frm = regFrom2()

    if request.method == "POST":
        frm = regFrom2(request.POST)

        if frm.is_valid():
            name = frm.cleaned_data["name"]
            username = frm.cleaned_data["username"]
            email = frm.cleaned_data["email"]
            password = frm.cleaned_data["password"]

            print("name: ", name)
            print("name: ", username)
            print("name: ", email)
            print("name: ", password)
    return render(request, "formval1/registration.html", {"frm": frm})
