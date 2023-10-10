from django.shortcuts import render
from .forms import StuDetailFrm, StaffForm
from django.contrib import messages


# Create your views here.
def show(request):
    data = {}
    if request.method == "POST":
        # data = StudentDetails(request.POST)
        # data.name = request.POST("name")
        # data.email = request.POST("email")
        # data.password = request.POST("password")
        # data.phone = request.POST("phone")

        frm = StuDetailFrm(request.POST)

        if frm.is_valid():
            frm.save()
            messages.add_message(request, messages.SUCCESS, "Detail Added Successfully")
            # or
            # messages.success(request, "Added successfully")
    else:
        frm = StuDetailFrm()



    return render(request, "crud/msg.html", {"frm": frm})


def add_staff_frm(request):
    frm = StaffForm()

    if request.method == "POST":
        frm = StaffForm(request.POST)
        if frm.is_valid():
            frm.save()
            # messages.add_message(request, messages.SUCCESS, "Staff Added Successfully")
            messages.success(request, "Staff Added")


    return render(request, "crud/staff.html", context={"form": frm})
