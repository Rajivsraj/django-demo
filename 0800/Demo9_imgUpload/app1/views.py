from django.shortcuts import render, HttpResponse
from .models import UploadImg

# Create your views here.
def abc(request):
    # return HttpResponse("hi")
    ok = UploadImg.objects.all()
    # request.Files
    if request.method == "POST":
        s = UploadImg()
        s.img = request.POST.get("img")
        s.save()
    return render(request, "app1/upload.html", {"data": ok})
