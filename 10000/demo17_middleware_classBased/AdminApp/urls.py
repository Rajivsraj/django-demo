from django.urls import path
from . import views

urlpatterns = [
    path("dashboard-a1/", views.dashboard, name="admin_dashboard"),
    path("profile/", views.profile, name="admin_profile"),
]