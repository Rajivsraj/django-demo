from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm
from .models import User


def home(request):
    return HttpResponse("<h1>Hi Home page</h1>")
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
    # return render(request, "validations/users-list.html")