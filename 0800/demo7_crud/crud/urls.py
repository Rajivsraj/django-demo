from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.add_student, name="addStu"),
    path("stu-list", views.list_student, name="stuList"),
    path("delete-stu/<int:stuid>", views.delete_student, name="stuDelete"),
    path("edit-stu/<stu_id>", views.edit_stu_view, name="name_edit_stu_view"),
    path("update-stu/", views.update_stu, name="name_update_stu"),
]
