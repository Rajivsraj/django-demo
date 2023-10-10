from django.contrib import admin
from .models import Employee, Employee2


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id", "name", "salary", "city"]

@admin.register(Employee2)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id", "name", "salary", "city"]
