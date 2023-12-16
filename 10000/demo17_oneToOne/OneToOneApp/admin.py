from django.contrib import admin
from .models import UserProfile, Course, Roles


# Register your models here.
@admin.register(UserProfile)
class AdminProfile(admin.ModelAdmin):
    list_display = ["user", "id", "city", "dept", "age", "phone", "gender"]


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ["user", "id", "course_name", "duration", "fees"]


@admin.register(Roles)
class AdminRoles(admin.ModelAdmin):
    list_display = ["id", "role_name"]


# @admin.register("onetooneapp_roles_user")
# class AdminJunction(admin.ModelAdmin):
#     list_display = ["id"]
