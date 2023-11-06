from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def mail_test(request):
    otp = 123
    link = f"settings.EMAIL_HOST_USER/{otp}"

    x = send_mail(
        "Test Mail",
        link,
        settings.EMAIL_HOST_USER,
        ["abhicrick1@gmail.com", settings.EMAIL_HOST_USER],
        fail_silently=False,
    )

    otp = request.GET.get("otp")
    print(x)
    return HttpResponse("hi")