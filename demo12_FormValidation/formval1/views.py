from django.shortcuts import render
from .forms import RegFormCls


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