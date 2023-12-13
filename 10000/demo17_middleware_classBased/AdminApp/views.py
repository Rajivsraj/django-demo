from django.shortcuts import render, HttpResponse


# Create your views here.
def dashboard(request):
    return HttpResponse("This is Admin Dashboard")


def profile(request):
    return HttpResponse("This is Admin Profile")