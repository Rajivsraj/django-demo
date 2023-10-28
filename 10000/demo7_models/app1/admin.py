from django.contrib import admin
from .models import Student, Studetn2

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "age", "phone"]


@admin.register(Studetn2)
class Student2Admin(admin.ModelAdmin):
    # list_display = ["name", "city", "city2", "city3"]
    list_display = ["name", "city", "city2", "city3"]
    # exclude = ["city3"]


