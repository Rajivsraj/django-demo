from django.shortcuts import render
from .models import Students


# Create your views here.
def add_student(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pasw = request.POST.get("pass")

        save_data = Students(fname=fname, lname=lname, password=pasw)
        save_data.save()
        
    return render(request, "form.html")