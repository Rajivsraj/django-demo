from django.urls import path
from . import views

urlpatterns = [
    path("reg/", views.usr_reg_fun)
]