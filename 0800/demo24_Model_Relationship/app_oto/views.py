from django.shortcuts import render
from django.contrib.auth.models import User
# from .models import StudentDetail, StudentMarksheet


# Create your views here.
# def show_data(request):
#     all_users = User.objects.all()
#     students = StudentDetail.objects.all()
#     marksheet = StudentMarksheet.objects.all()
#     for x in marksheet:
#         print(x.student_detail.user)
#     return render(request, "data.html", context={"users": all_users, "students": students, "marksheet": marksheet})