from django.urls import path
from . import views


urlpatterns = [
    path("", views.set_session, name="set-session"),
    path("get-session/", views.get_session, name="get-session"),
    path("logout/", views.logout, name="del-session"),
]