from django.shortcuts import reverse, render, redirect, HttpResponseRedirect
# from .views import profile
from django.utils.decorators import decorator_from_middleware


class my_middleware:
    print("It will run once")

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "username" not in request.session:
            return redirect("login")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

session_check = decorator_from_middleware(my_middleware)