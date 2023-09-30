from django.shortcuts import render
from .models import Employee


# Create your views here.
def query_set(request):
    # all_emp = Employee.objects.all()    # select * from table;
    # print(all_emp)
    # print(all_emp.query)
    # return render(request, "app1/data.html", context={"employees": all_emp})

    # all_emp = Employee.objects.filter(name="Rahul") # Case Sensitive
    # all_emp = Employee.objects.filter(city="new delhi")
    # all_emp = Employee.objects.filter(city="new delhi", id=3)
    # all_emp = Employee.objects.filter(city="Goa") # if record not found than return querySet[]
    # print(all_emp)
    # print(all_emp.query)

    # all_emp = Employee.objects.exclude(city="new delhi")
    # print(all_emp)
    # print(all_emp.query)

    # all_emp = Employee.objects.order_by("city", "name")
    # print(all_emp)
    # print(all_emp.query)

    # all_emp = Employee.objects.order_by("id").reverse()
    # all_emp = Employee.objects.order_by("name").reverse()
    # all_emp = Employee.objects.order_by("name").reverse()[5:10]
    # all_emp = Employee.objects.order_by("id")
    # for x in all_emp:
    #     print(x.name[:3])
    # print(all_emp)
    # print(all_emp.query)

    # all_emp = Employee.objects.values()
    # all_emp = Employee.objects.values("name", "city")
    # all_emp = Employee.objects.values(name=upperCase("name")) # need to check again
    # print(all_emp)
    # print(all_emp.query)

    all_emp = Employee.objects.values_list()
    print(all_emp)
    # for x in all_emp:
    #     for y in x:
    #         print(y, end=" ")
    #
    #     print()
    print(all_emp.query)
    return render(request, "app1/data.html", context={"employees": all_emp})


