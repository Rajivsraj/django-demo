from django.shortcuts import render
from .models import Employee, Employee2
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group


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

    # all_emp = Employee.objects.values_list()
    # print(all_emp)
    # for x in all_emp:
    #     for y in x:
    #         print(y, end=" ")
    #
    #     print()
    # print(all_emp.query)
    # st = set()
    # all_emp = Employee.objects.all()
    # all_emp = list(s)
    # print(all_emp.query)

    # all_emp = Employee.objects.dates("date", kind="month")
    # print(all_emp)
    # print(all_emp.query)

    # tbl1 = Employee.objects.values_list("name")
    # tbl2 = Employee2.objects.values_list("name")
    # all_emp = tbl1.union(tbl2, all=True)
    # print(all_emp)
    # print()
    # # print(all_emp.query)
    # print(tbl1)
    # print(tbl2)
    # return render(request, "app1/data.html", context={"employees": ""})

    # get()
    # ==============
    # sq = Employee.objects.get(pk=1)
    # sq = Employee.objects.get(emp_id=102)
    # sq = Employee.objects.get(emp_id=111)

    # sq = Employee.objects.get(emp_id=111)
    # try:
    #     sq = Employee.objects.get(emp_id=111)
    # except ObjectDoesNotExist as e:
    #     if e:
    #         e = "Data Not Found"
    #     return render(request, "app1/data.html", context={"error": e})

    # sq = Employee.objects.first()
    # sq = Employee.objects.last()
    # sq = Employee.objects.latest("city")
    # sq = Employee.objects.earliest("date")
    # sq = Employee.objects.exists()
    # sq = Group.objects.exists() # check table have some data or not
    # print(sq)
    return render(request, "app1/data.html", context={"single": sq})