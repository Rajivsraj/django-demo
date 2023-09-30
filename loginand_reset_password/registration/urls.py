from django.urls import path 
from django.contrib import admin
from app import views

urlpatterns = [

    path('admin/', admin.site.urls, ),
    path('dashboard/', views.dashboard, name="dashboard"),
    path("register/", views.registration, name ="singup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("profile/", views.user_profile, name="user_profile"),
]
