from django.shortcuts import render
from .models import Employee, Employee2
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.db.models import Sum, Min, Max, Avg, Count


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

# ============================================================= Union ======================================================

    # tbl1 = Employee.objects.values_list("name")
    # tbl2 = Employee2.objects.values_list("name")
    # all_emp = Employee.objects.all().values_list("name").union(Employee2.objects.all().values_list("name")) # This is inline and it returns tuple inside the queryset
    # all_emp = Employee.objects.all().values("name").union(Employee2.objects.all().values("name")) # This is inline and it returns key value pair inside the queryset

    # all_emp = tbl1.union(tbl2, all=True) It returns all the values including duplicate 
    # all_emp = tbl1.union(tbl2, all=False) It returns only the unique values excluding duplicate 
    # print(all_emp)
    # print()
    # print()

    # return render(request, "app1/data.html", context={"employees": ""})

# ============================================================= UnionEnd ======================================================

# ============================================================= Intersection ======================================================
    # tbl1 = Employee.objects.values_list("name")
    # tbl2 = Employee2.objects.values_list("name")
    # all_emp = tbl1.intersection(tbl2) # It returns tuple inside the queryset
    # all_emp = Employee.objects.all().values("name").intersection(Employee2.objects.all().values("name")) # This is inline and it returns key value pair inside the queryset

    # print(all_emp)
    # print()
    # print()

# ============================================================= IntersectionEnd ====================================================

    # tbl1 = Employee.objects.values_list("name")
    # tbl2 = Employee2.objects.values_list("name")
    # all_emp = Employee.objects.all().values_list("name").union(Employee2.objects.all().values_list("name")) # This is working and it returns tuple inside the queryset
    # # all_emp = Employee.objects.all().values("name").union(Employee2.objects.all().values("name")) # This is working and it returns tuple inside the queryset
    # # all_emp = tbl1.union(tbl2, all=True) # This is not working
    # print(all_emp)
    # print()
    # print()
    # print(end='==========================================')
    # print(all_emp.query)
    # print(tbl1) 
    # print(tbl2)
    # return render(request, "app1/data.html", context={"employees": all_emp})


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
    # return render(request, "app1/data.html", context={"single": sq})

    # ct = Employee.objects.create(emp_id=127, name="Rajat", city="Pune")
    # ct = Employee.objects.create(emp_id=128, city="Bangalore")
    # return render(request, "app1/data.html", context={"single": ct})

    # data, created = Employee.objects.get_or_create(emp_id=129, name="Vaibhav", city="Chennai")
    # data, created = Employee.objects.get_or_create(emp_id=126, name="Raman", salary=348908, city="Pune")
    # print(data, created)

    # single = Employee.objects.filter(pk=1)
    # res = single.update(emp_id=130, name="Saxena", salary=648908, city="Himalya")
    # print(single)
    # print(res)

    # data = Employee.objects.filter(pk=1).update(emp_id=130, name="Lalit", salary=6489098, city="Himalya")
    # data = Employee.objects.update(id=18, emp_id=130, name="Saxena", salary=648908, city="Himalya")
    # print(data)

    # data = Employee.objects.get(name="").delete()
    # print(data)
    # data = Employee.objects.filter(salary=None).delete()
    # print(data)
    # not working properly - res, bul = Employee.objects.update_or_create(defaults={"city": "Punjab", "name": "Bhaskar"})

    # emps = [
    #     Employee.objects.create(emp_id=133, name="Abhishek", city="New Delhi", salary=94544),
    #     Employee.objects.create(emp_id=134, name="Ankit", city="New Delhi", salary=54656),
    #     Employee.objects.create(emp_id=135, name="Aditya", city="New Delhi", salary=5466),
    # ]
    # res = Employee.objects.bulk_create(emps, ignore_conflicts=True)
    # print(res)

    # all = Employee.objects.all()
    # for emp in all:
    #     # print(emp["emp_id"])
    #     emp.name = "Vikram"
    #
    # Employee.objects.bulk_update(all, ["name"])

    # s = Employee.objects.get(pk=34)
    # s.delete()

    # c = Employee.objects.filter(name="Vikram").count()
    # c = Employee.objects.filter(salary__gte=50000).count()
    # c = Employee.objects.filter(salary__gte=50000).delete()
    # print(c)

    # data = Employee.objects.filter(salary__gte= 1000)
    # print(data)
    total_sal = Employee.objects.all().aggregate(Count("name"))
    data = total_sal
    print(data)
    return render(request, "app1/data.html", context={"single": data})
    # return render(request, "app1/data.html", context={"single": ""})
