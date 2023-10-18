from django.shortcuts import render


# Create your views here.
def form_page(request):
    # print(request)
    # print(request.GET.get("fname"))
    #     # OR
    # print(request.GET["fname"])

    # print(request)
    # # request.GET["fname"]
    # fname = request.GET.get("fname")
    # lname = request.GET.get("lname")
    # age = request.GET.get("age")
    # city = request.GET.get("city")
    # salary = request.GET.get("salary")
    # print(fname, lname, age, city, salary)


    # Data Exit in form
    # print(request)
    # request.GET["fname"]
    # fname = request.GET.get("fname")
    # lname = request.GET.get("lname")
    # age = request.GET.get("age")
    # city = request.GET.get("city")
    # salary = request.GET.get("salary")
    # print(fname, lname, age, city, salary)
    data = request.GET

    return render(request, "form.html", context={"data": data})