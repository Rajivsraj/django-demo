from django.shortcuts import render


# Create your views here.
def stu_atten(request):
    return render(request, "attendance/add-attendance.html")


def update_atten(request):
    return render(request, "attendance/update-attendance.html")