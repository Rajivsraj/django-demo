from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def home(request):
    res = send_mail(
        subject="Test Mail",
        message="Hi This si Test mail",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["rajivsraj78@gmail.com"],
        fail_silently=False,
    )

    print(res)

    return render(request, template_name="home.html")