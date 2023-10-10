from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.StudentDetails)
class AdminStudentDetail(admin.ModelAdmin):
    list_display = ["name", "email", "password", "phone"]


@admin.register(models.AddStaff)
class AdminAddStaff(admin.ModelAdmin):
    list_display = ["name", "age"]
