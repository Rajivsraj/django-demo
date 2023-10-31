from django.shortcuts import render
from django.contrib.auth.models import User
# from .models import StudentDetail, StudentMarksheet
from .models import Course

# Create your views here.
# def show_data(request):
#     all_users = User.objects.all()
#     students = StudentDetail.objects.all()
#     marksheet = StudentMarksheet.objects.all()
#     for x in marksheet:
#         print(x.student_detail.user)
#     return render(request, "data.html", context={"users": all_users, "students": students, "marksheet": marksheet})

def show_rec(request):
    # all = Course.objects.all()
    #
    # ankit_course = Course.objects.filter(user__username="ankit")
    #
    # all_users = User.objects.all()
    #
    # c_by_user = User.objects.filter(course__course_name="sw")
    # print(c_by_user)


    all = Course.objects.all()
    # ankit_course = Course.objects.filter(hello__username="ankit")

    ankit_course = Course.objects.filter(course_name="sw")

    # c_by_user = User.objects.filter(course__course_name="sw")
    # print(c_by_user)
    return render(request, "showdata.html", context={"data": all, "ankit": ankit_course})
    # return render(request, "showdata.html", context={"data": all, "ankit": ankit_course, "users": all_users, "sw": c_by_user})