from django.shortcuts import render
from .models import StudentDetails
from django.http import HttpResponseRedirect


# Create your views here.
def add_student(request):
    msg = {}

    if request.method == "POST":
        data = StudentDetails()
        if request.POST.get("fname") == "":
            msg["error"] = "Provide Fname"
        else:
            data.fname = request.POST.get("fname")

        data.lname = request.POST.get("lname")
        data.password = request.POST.get("password")
        data.email = request.POST.get("email")
        data.phone = request.POST.get("phone")
        if msg["error"]:
           pass
        else:
            msg["status"] = "data Saved"
            data.save()

    return render(request, "crud/add-student.html", context={"old_data": request.POST, "save_status": msg})


def list_student(request):
    all_data = StudentDetails.objects.all()
    return render(request, "crud/student-list.html", {"all_students_data": all_data})


def delete_student(request, stuid):
    stu_id = stuid
    x = StudentDetails.objects.get(pk=stu_id)
    x.delete()
    return HttpResponseRedirect("/stu-list")
