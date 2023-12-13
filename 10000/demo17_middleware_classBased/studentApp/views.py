from django.shortcuts import render, HttpResponse


# Create your views here.
def dashboard(request):
    return HttpResponse("This is Student Dashboard")


def profile(request):
    return HttpResponse("This is Student Profile")