from django.urls import path
from . import views

urlpatterns = [
    path("middle/<int:stuid>", views.test_middleware_fun)
]