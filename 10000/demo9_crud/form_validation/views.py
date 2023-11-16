from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .forms import RegistrationForm
from .models import User


def home(request):
    return render(request, "validations/home.html")
    # return HttpResponse("<h1>Hi Home page</h1>")
# after form submission successfully data should not be shown into the field
# Create your views here.
def register(request):
    msg = False
    if request.method == "POST":
        frm = RegistrationForm(request.POST)
        if frm.is_valid():
            fname = frm.cleaned_data.get("first_name")
            username = frm.cleaned_data.get("username")
            phone = frm.cleaned_data.get("phone")
            email = frm.cleaned_data.get("email")
            password = frm.cleaned_data.get("password")
            usr = User(first_name=fname, username=username, phone=phone, email=email, password=password)
            print("before save: ", usr)
            usr.save()
            print("after save: ", usr)
            print("data saved")
            msg = "?msg=true"
            return HttpResponseRedirect("/register/"+msg)
        else:
            print("Invalid data")
    else:
        frm = RegistrationForm()
        if request.GET.get("msg"):
            return render(request, "validations/registration.html", context={"frm": frm, "msg": True})

        return render(request, "validations/registration.html", context={"frm": frm})


def users_list(request):
    all_users = User.objects.all()
    return render(request, "validations/users-list.html", context={"users": all_users})


def delete_user(request, id):
    # user = User.objects.get(id=id)
    obj = User(id=id)
    obj.delete()
    return HttpResponseRedirect("/users-list/")


def update_user(request, id):
    usr = User.objects.get(id=id)
    # RegistrationForm({"first_name": usr.first_name, })
    frm = RegistrationForm(data=usr.__dict__)

    if request.method == "POST":
        frm = RegistrationForm(request.POST)
        if frm.is_valid():

            print(frm.cleaned_data)
            # User(first_name=frm.cleaned_data.get("first_name"))
            # s = User(frm.cleaned_data).save()
            # s.save()
            #     OR
            fn = frm.cleaned_data.get("first_name")
            username = frm.cleaned_data.get("username")
            phone = frm.cleaned_data.get("phone")
            email = frm.cleaned_data.get("email")
            pass1 = frm.cleaned_data.get("password")
            # pass2 = frm.cleaned_data.get("password2")

            # this will update record, because it will check pk, if it is already exists in table then record will be update else will add new red
            obj = User(pk=id, first_name=fn, username=username, phone=phone, email=email, password=pass1)
            obj.save()
            return redirect("users_list")
    return render(request, "validations/update-user.html", context={"frm": frm})
    # return HttpResponseRedirect("/users-list/")
