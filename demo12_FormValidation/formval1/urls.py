from django.urls import path
from . import views


urlpatterns = [
    path("registration/", views.regFormFun),
    path("registration2/", views.regFormFun2)
]