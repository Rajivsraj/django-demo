from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.reg_form),
]