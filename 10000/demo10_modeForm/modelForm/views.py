from django.shortcuts import render
from .models import Register
from .forms import RegistrationForm, StudentForm, TeacherForm


def student_details(request):
    frm = StudentForm()
    return render(request, "student.html", context={"form": frm})


def teacher_details(request):
    frm = TeacherForm()
    frm.order_fields(["teacher_name", "username","phone"])
    return render(request, "teacher.html", context={"form": frm})


# Create your views here.
def user_registration(request):
    frm = RegistrationForm()

    if request.method == "POST":
        frm = RegistrationForm(request.POST)
        print(frm)
        print(request)
        if frm.is_valid():
            print("data valid")
        else:
            print("data not valid")

    return render(request, "register.html", {"form": frm})