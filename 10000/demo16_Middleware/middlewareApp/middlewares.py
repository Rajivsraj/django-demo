from django.shortcuts import reverse, render, redirect, HttpResponseRedirect
from .views import profile


def my_middleware(get_response):
    print("It will run once")

    def inner_fun(request):
        print("before")
        res = get_response(request)
        print("After")
        return res


    return inner_fun
