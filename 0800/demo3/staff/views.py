from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def hra(request):
    return render(request, "salary/hra.html")


def da(request):
    return render(request, "salary/da.html")