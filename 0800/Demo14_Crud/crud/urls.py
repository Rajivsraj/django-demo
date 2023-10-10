from django.urls import path
from . import views

urlpatterns = [
    path("", views.show, name="home"),
    path("add-staff/", views.add_staff_frm)
]