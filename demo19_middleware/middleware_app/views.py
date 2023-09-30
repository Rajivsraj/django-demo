from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test_middleware_fun(request, stuid):
    print("This is view fun", stuid)
    return HttpResponse("<h1> Hello </h1>")
