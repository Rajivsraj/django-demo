from django.urls import path
from . import views

urlpatterns = [
    path("reg/", views.regForm),
    path("reg2/", views.regForm2)
]