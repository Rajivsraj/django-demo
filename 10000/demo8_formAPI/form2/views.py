from django.shortcuts import render
from .forms import RegistrationForm


# Create your views here.
def register_frm_api(request):
    frm = RegistrationForm()
    return render(request, "frm1.html", context={"form": frm})


def register_id_attr(request):
    # frm = RegistrationForm(auto_id=True)
    # frm = RegistrationForm(auto_id=False)
    # frm = RegistrationForm(auto_id="%s_hello", label_suffix="=")
    # frm = RegistrationForm(auto_id="%s_hello", prefix="Mohan")

    # data = {
    #     "first_name": "Mohan",
    #     "last_name": "Babu",
    #     "password": "Hello@123"
    # }
    # frm = RegistrationForm(auto_id="%s_hello", prefix="Mohan", initial=data)

    frm = RegistrationForm(auto_id="%s_hello", prefix="Mohan", field_order=["last_name"])
    return render(request, "frmAttr.html", context={"form": frm})


def register_frm2(request):
    data = {
        "first_name": "Suraj"
    }
    frm = RegistrationForm(initial=data)

    # print(frm.first_name.required)
    return render(request, "frm2.html", context={"form": frm})
