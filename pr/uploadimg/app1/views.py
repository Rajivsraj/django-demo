from django.shortcuts import render
from .models import UploadImg
from django.conf import settings

x = settings.MEDIA_URL
# Create your views here.
def add_img(request):

    if request.method == "POST":
        up = UploadImg()
        up.name = request.POST.get("name")
        if len(request.FILES) != 0:
            print(request.FILES["img"])
            up.img = request.FILES["img"]

        up.save()

    return render(request, "app1/img.html", {"img": all, "x":x})
