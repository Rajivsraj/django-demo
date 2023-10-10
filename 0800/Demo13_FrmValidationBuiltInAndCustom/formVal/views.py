from django.shortcuts import render
from .forms import FormVal


# Create your views here.
def usr_reg_fun(request):
    frm = FormVal

    if request.method == "POST":
        frm = FormVal(request.POST)

        if frm.is_valid():
            fname = frm.cleaned_data["fname"]
            lname = frm.cleaned_data["lname"]
            print(fname, lname)
    return render(request, "formVal/reg.html", context={"frm": frm})
