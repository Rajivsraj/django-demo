from django.shortcuts import render


# Create your views here.
def add_attendance(request):
    return render(request, "attendance/attendance.html")