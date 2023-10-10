from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def set_cookie(request):
    res = render(request, "cookies/set.html")
    # res.set_cookie("name", "Rahul", max_age=10)
    res.set_cookie("name", "Rahul", expires=datetime.utcnow()+timedelta(days=365))
    print(res)
    return res


def get_cookie(request):
    # g_cookie = request.COOKIES["name"]
    g_cookie = request.COOKIES.get("name")
    return render(request, "cookies/get.html", {"cookie":g_cookie})


def del_cookie(request):

    res = render(request, "cookies/set.html")
    res.delete_cookie("name")
    return res