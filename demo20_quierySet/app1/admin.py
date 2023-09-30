from django.contrib import admin
from .models import Employee, Student


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id", "name", "salary", "city"]

@admin.register(Student)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["stu_id", "name", "result", "city"]