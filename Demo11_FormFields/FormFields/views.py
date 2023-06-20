from django.shortcuts import render
from .forms import StuReg
from .from2 import StuRegFrm
from .models import StuRegModel

# Forms with DB
def RegFrm(request):
    frm = StuRegFrm()

    if request.method == "POST":
        frm = StuRegFrm(request.POST)
        data = StuRegModel()
        # print("hi")
        # if frm.is_valid():
        #     # data.name = frm.cleaned_data['name']
        #     # data.email = frm.cleaned_data['email']
        #     # data.password = frm.cleaned_data['password']
        #     name = frm.cleaned_data['name']
        #     email = frm.cleaned_data['email']
        #     password = frm.cleaned_data['password']
        #     # data.save({"name": name, "email":email, "password":password})
        #     # StuRegModel(name=name, email=email, password=password).save()
        #     data = StuRegModel(name=name, email=email, password=password).save()
        #     # data.save()

        # DELETE RECORD
        if frm.is_valid():
            name = frm.cleaned_data['name']
            email = frm.cleaned_data['email']
            password = frm.cleaned_data['password']
            data = StuRegModel(id=2)
            data.delete()
            
    # or DELETE RECORD
    # data = StuRegModel(id=2)
    # data.delete()

    # UPDATE RECORD
        if frm.is_valid():
            name = frm.cleaned_data['name']
            email = frm.cleaned_data['email']
            password = frm.cleaned_data['password']
            data = StuRegModel(id=3, name=name, email=email, password=password)
            data.save()
    return render(request, "FormFields/stu-reg.html", {"frm": frm})


# Create your views here.
# def stu_reg(request):

#     frm = StuReg()

#     if request.method == "POST":

#         frm = StuReg(request.POST)

#         # if frm.is_bound:
#             # print("data blank found")
#         if frm.is_valid():
#             print("hi valid")
#             fname = frm.cleaned_data["name"]
#             if len(fname) >= 5:
#                 err = ">5 char"
#             print(f"name: {fname}")
   
#     return render(request, "FormFields/stu_reg.html", context={"frm": frm})


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