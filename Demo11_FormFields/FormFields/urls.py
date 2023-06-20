from django.urls import path
from . import views

urlpatterns = [
    # path("reg/", views.stu_reg),
    path("registration/", views.RegFrm)

]