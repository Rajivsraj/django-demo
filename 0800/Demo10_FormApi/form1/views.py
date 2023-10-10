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
    #     "email": "lsdjf@lsdf.sdf"
    # }
    # frm = StuRegistrationFrmApi(data) # using this we can add prefix to the id value of label attribute
    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute
    # x = frm.is_bound    # if data exists in form it return the true wether data is correct or not
    # y = frm.is_valid()  # if it return true if data is valid/correct
    # print(x)
    # print(y)

    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute

    # frm = StuRegistrationFrmApi(data) # using this we can add prefix to the id value of label attribute
    # if frm.is_bound:
    #     print("ok hai")
    #     if frm.is_valid():
    #         print("data also valid")


    # a Look of form validation
    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute
    # if request.method == "POST":
    #     print(request.POST)
    #     fname = request.POST.get("lname")
    #     frm = StuRegistrationFrmApi(request.POST)

    # frm = StuRegistrationFrmApi() # using this we can add prefix to the id value of label attribute


    # if request.method == "POST":
    #     # fname = request.POST.get("fname")
    #     # password = request.POST.get("password")
    #     # city = request.POST.get("city")
    #
    #     # print(f"Fname: {fname} Pass: {password} city {city}")
    #     print(request.POST)
    #     frm = StuRegistrationFrmApi(request.POST)

    # data = {
    #     "fname": "Rahul",
    #     "lname": "Kumar"
    # }
    # frm = StuRegistrationFrmApi(initial=data)
    #
    frm = StuRegistrationFrmApi()
    if request.method == "POST":
        frm = StuRegistrationFrmApi(data=request.POST)
        print(request.POST)
    return render(request, "form1/registration.html", context={"frm": frm})
