from django.shortcuts import render
from .forms import Form1

# after form submission successfully data should not be shown into the field
# Create your views here.
def frm_validation(request):

    if request.method == "GET":
        frm = Form1()
    else:
        frm = Form1(request.POST)
        if frm.is_valid():
            fname = frm.cleaned_data.get("fname")
            lname = frm.cleaned_data.get("lname")
            email = frm.cleaned_data.get("email")
            phone = frm.cleaned_data.get("phone")
            print(fname, lname, email, phone)
        else:
            print("Invalid data")

    return render(request, "validations/frm1.html", context={"frm": frm})
