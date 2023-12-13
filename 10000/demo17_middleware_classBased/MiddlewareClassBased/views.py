from django.shortcuts import render


# Create your views here.
def home(request):
    print("This is view function")
    return render(request, template_name="home.html")
