from django.shortcuts import render


# Create your views here.
def ok(request):
    return render(request, "one/home.html")


def student(request):
    return render(request, "one/student.html")