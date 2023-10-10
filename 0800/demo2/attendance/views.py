from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    table = "<table border='1'> " \
            "<tr> " \
                "<td> sr. no </td> " \
                "<td> name </td> " \
                "<td> City </td> " \
                "<td> Dept </td> " \
                "<td> marks </td> " \
            "</tr> " \
            "</table>"

    h1 = "<h1> Hello Student list </h1>"
    p = "<p> Hello para </p>"

    data = {
        "one": h1,
        "two": p,
        "three": table
    }

    return HttpResponse(data.get("one"))


def about(requst):
    return HttpResponse("<h1>hello  about</h1>")


def contact(request):
    return HttpResponse("<h1> Contact us</h1>")


