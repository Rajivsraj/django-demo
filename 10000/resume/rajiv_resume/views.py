from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "rajiv_resume/home.html")


def about(request):
    return render(request, "rajiv_resume/about.html")


def resume(request):
    return render(request, "rajiv_resume/resume.html")


def services(request):
    return render(request, "rajiv_resume/services.html")


def portfolio(request):
    return render(request, "rajiv_resume/portfolio.html")


def contact(request):
    return render(request, "rajiv_resume/contact.html")
