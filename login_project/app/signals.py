from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User


def login_success(sender, request, user, **kwargs):
    print("logged in successfully")
    print("Sender: ", sender)
    print("request: ", request)
    print("user: ", user.password)
    print("**kwar: ", kwargs)


user_logged_in.connect(login_success, sender=User)
