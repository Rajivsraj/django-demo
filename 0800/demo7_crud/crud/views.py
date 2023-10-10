from django.shortcuts import render, redirect
from .models import StudentDetails
from django.http import HttpResponseRedirect, HttpResponse


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
        if len(msg) >= 1:
           msg["status"] = "cant be saved"
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


def edit_stu_view(request, stu_id):
    data = {}
    data["status"] = ""
    edit = StudentDetails.objects.filter(id=stu_id).first()
    if edit is None:
        data["status"] = "Record not found"
    else:
        data["single_rec"] = edit
    return render(request, "crud/edit-stu.html", context={"data": data})


def update_stu(request):
    stu_id = request.POST.get("stu_id")
    updt = StudentDetails.objects.filter(id=stu_id).first()
    updt.fname = request.POST.get("fname")
    updt.lname = request.POST.get("lname")
    updt.email = request.POST.get("emali")
    updt.password = request.POST.get("password")
    updt.phone = request.POST.get("phone")
    updt.save()
    return redirect("stuList")

