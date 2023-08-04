from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registration, name="registration"),
    path("login/", views.user_login, name="login"),
]