from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from middlewareApp.middlewares import my_middleware
from django.utils.decorators import decorator_from_middleware


# Create your views here.
def home(request):
    print("this is view function")
    request.session["username"] = "abhi01"
    request.session["email"] = "abhi01@gmail.com"
    return render(request, template_name="home.html")


def login(request):
    return HttpResponse("Login")


def profile(request):
    print("profile function done")
    p_data = "hello profile"

    return render(request, template_name="profile.html", context={"data": p_data})
