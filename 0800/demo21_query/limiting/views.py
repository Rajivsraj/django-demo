from django.shortcuts import render
from q_object.models import Student


# Create your views here.
def limiting(request):
    # cant use negative slicing
    # rec_5 = Student.objects.all()[:3]
    # rec_5 = Student.objects.all()[1:4]
    rec_5 = Student.objects.all()[::2]
    return render(request, "limit.html", context={"data": rec_5})