from django.shortcuts import render
from .forms import StuRegistrationFrmApi


# Create your views here.
def registration(request):
    # frm = StuRegistrationFrmApi(auto_id=True)
    # frm = StuRegistrationFrmApi(auto_id=False) # removes the label tag not label value
    # frm = StuRegistrationFrmApi(auto_id="rsu_%s") # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi(label_suffix="Ok") # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi(prefix="ok") # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi(initial={
    #     "fname": "Sumit",
    #     "lname": "Kumar",
    # }) # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute
    # frm.order_fields(["lname", "fname"])   # It will change the sequence of form

    # data={
    #     "fname": "Lalit",
    #     "lname": "Suraj",
    #     "email": "lsdjf",
    # }
    # frm = StuRegistrationFrmApi(data) # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute
    # x = frm.is_bound    # if data exists in form it return the true wether data is correct or not
    # y = frm.is_valid()  # if it return true if data is valid/correct
    # print(x)
    # print(y)

    frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute

    return render(request, "form1/registration.html", context={"frm": frm})
