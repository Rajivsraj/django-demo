from django.shortcuts import render
# Manual add
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello heading 1 </h1>")


def about_page(request):
    return HttpResponse("This is about page")


def my_file(request):
    return render(request, "index.html")
