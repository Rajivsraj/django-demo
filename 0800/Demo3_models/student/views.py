from django.shortcuts import render
from .models import Student


# Create your views here.
def stu_list(request):
    all_data = Student.objects.all()
    for x in all_data:
        print(x.id)
    return render(request, "student/student-list.html", {"data":all_data})