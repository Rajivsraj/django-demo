from django.shortcuts import render
# from .forms import RegistrationForm


# 04/11/2023 - Form Validation
from .forms import RegistrationFormValidation


def register_frm_validation(request):

    if request.method == "POST":
        frm = RegistrationFormValidation(request.POST)

        if frm.is_valid():
            # fullname = request.POST.get("fullname")

            fullname = frm.cleaned_data["fullname"]
            # fullname = frm.cleaned_data["fullnamea"]  # will give error if key not found
            username = frm.cleaned_data.get("fullnamea")
            fullname = frm.cleaned_data.get("fullnamea")    # will return None if key not found

            print(fullname)

        print("Post Method")
        print(frm)
    else:
        frm = RegistrationFormValidation()
        print("Get Method")
        print(frm)

    return render(request, "validation.html", context={"frm": frm})



# Create your views here.
# def register(request):
#     frm = RegistrationForm(request.GET)
#     username = request.GET.get("username")
#
#     print(username)
#     return render(request, "form3.html", context={"frm": frm})


