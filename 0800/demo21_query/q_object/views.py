from django.shortcuts import render
from .models import Student
from django.db.models import Q


# Create your views here.
def student(request):
    # all_stu = Student.objects.all()
    # return render(request, "student.html", context={"data": all_stu})

    # con = Student.objects.filter(Q(age__gte=21) & Q(city="delhi"))
    # con = Student.objects.filter(Q(age__gte=21))
    # con = Student.objects.filter(Q(age__gte=21) | Q(city="delhi"))
    # con = Student.objects.filter(age__gte=21, city="delhi")
    con = Student.objects.filter(Q(age__gte=21) | Q(city="delhi")) & Student.objects.filter(~Q(city="pune"))
    print(con)
    print(con.query)
    return render(request, "student.html", context={"data": con})
