from django.shortcuts import render


# Create your views here.
def store(request):
    return render(request, "login.html")


def cart(request):
    a = 10
    b = 20
    total = a+b
    data = {
        "val1": a,
        "val2": b,
        "kul": total
    }
    return render(request, "cart.html", {"record": data})