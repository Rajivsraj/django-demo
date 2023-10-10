from django.urls import path
from . import views

urlpatterns = [
    path("attendnace/", views.add_attendance)
]