from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registration, name="registration"),
    path("login/", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logut, name="logout"),
    path("password-reset/", views.resetPassword, name="password-reset"),
    path("profile/", views.user_profile, name="profile"),
]