from django.urls import path
from . import views


urlpatterns = [
    path("set/", views.set_cookie, name="set-cookie"),
    path("del/", views.del_cookie, name="del-cookie"),
    path("get/", views.get_cookie, name="get-cookie")
]