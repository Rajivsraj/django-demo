from django.shortcuts import render
from .models import StudentDetails

# Create your views here.
def show(request):
    data={}
    if request.method == "POST":
      data =  StudentDetails(request.POST)
      data.name = request.POST("name")
      data.email = request.POST("email")
      data.password = request.POST("password")
      data.phone = request.POST("phone")

      data.save()

    return render(request, "crud/action.html")

