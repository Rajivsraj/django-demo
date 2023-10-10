from django.urls import path
from . import views

urlpatterns = [
    path("attendance/", views.stu_atten),
    path("update-attendance/", views.update_atten),
]
