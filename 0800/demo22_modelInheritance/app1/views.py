from django.shortcuts import render
from .models import Faculty, Student, Child, Parents, Husband, Wife
# Create your views here.


def Stu(request):
    data = Student.objects.all()
    return render(request,"student.html",context={"all":data})



def Add_faculty(request):
    data2 = Faculty.objects.all()
    return render(request,"faculty.html",context={"all":data2})


def Add_Parents(request):
    data3 = Parents.objects.all()
    return render(request,"parents.html",context={"all":data3})


def Add_Child(request):
    data4 = Child.objects.all()
    return render(request,"child.html",context={"all":data4})


def Add_Wife(request):
    data5 = Wife.objects.all()
    return render(request,"wife.html",context={"all":data5})


def Add_Husband(request):
    data6 = Husband.objects.all()
    return render(request,"husband.html",context={"all":data6})