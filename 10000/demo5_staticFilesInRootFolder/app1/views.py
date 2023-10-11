from django.shortcuts import render


# Create your views here.
def xyz_page(request):
    return render(request, "xyz.html")
