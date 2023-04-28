from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.add_student, name="addStu"),
    path("stu-list", views.list_student, name="stuList"),
    path("delete-stu/<int:stuid>", views.delete_student, name="stuDelete"),
]
