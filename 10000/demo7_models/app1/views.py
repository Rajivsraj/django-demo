from django.shortcuts import render
from .models import Studetn2

# Create your views here.
def show_rec(request):
    # READ
    all = Studetn2.objects.all()
    # all = Studetn2.objects.filter(city="delhi")

    # CREATE
    # Add New Record
    # obj = Studetn2()
    # obj.name = "Lalit"
    # obj.city = "Normal city"
    # obj.city2 = "this is city 2"
    # obj.city3 = "this is city 3"
    # obj.save()
    # J

    # OR
    x = Studetn2(name="Shiristi", city="one", city2="two", city3="three")
    x.save();
        # OR
    Studetn2(name="Shiristi", city="one", city2="two", city3="three").save()
        #  OR
    return render(request, "data.html", context={"students": all})
