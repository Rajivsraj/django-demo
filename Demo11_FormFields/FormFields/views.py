from django.shortcuts import render
from .forms import StuReg


# Create your views here.
def stu_reg(request):

    frm = StuReg()

    if request.method == "POST":

        frm = StuReg(request.POST)

        # if frm.is_bound:
            # print("data blank found")
        if frm.is_valid():
            print("hi valid")
            fname = frm.cleaned_data["name"]
            if len(fname) >= 5:
                err = ">5 char"
            print(f"name: {fname}")
   
    return render(request, "FormFields/stu_reg.html", context={"frm": frm})


# def stu_reg(request):
#     data = {
#         "name": "Rahul"
#     }
#     frm = StuReg()

#     if request.method == "POST":
#         frm = StuReg(data=request.POST, initial=data)

#         if frm.has_changed():
#             print("changed data")
#             print(request.POST)

#             if request.POST.get("name") == "Rahul":
#                 print("lklllllllllllllllllll")
#         else:
#             print("You haven't changed anything")

#     return render(request, "FormFields/stu_reg.html", context={"frm": frm}