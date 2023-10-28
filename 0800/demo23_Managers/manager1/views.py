from django.shortcuts import render
from .models import Student


# Create your views here.
# def show_stu_details(request):
#     all_stu = Student.myManger.all()
#     # all_stu = Student.objects.all()
#     return render(request, "students.html", context={"data": all_stu})


def show_stu_details(request):
    # all_stu = Student.myManger.all()
    # all_stu = Student.objects.all()
    all_stu = Student.myCustomManager.all()
    print(all_stu)
    return render(request, "students.html", context={"data": all_stu})