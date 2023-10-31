from django.contrib import admin
# from .models import StudentDetail
# from .models import StudentMarksheet


# Register your models here.
# @admin.register(StudentDetail)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["user", "age", "city"]


# @admin.register(StudentProfile)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["age", "city", "user"]
#
#
# @admin.register(StudentMarksheet)
# class StudentMarksheetAdmin(admin.ModelAdmin):
#     pass
# list_display = ["student_detail", "maths", "science", "english", "skt", "total", "average"]


# One To Many
# ========================================================================
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["user", "course_name", "duration"]

# -------------------------
# from .models import Category, Product
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["cat_name"]
#
#
# @admin.register(Product)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["product_name", "price", "category", "user"]


# from .models import Teacher, Student
#
#
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ["t_name", "quali", "salary"]
#
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ["s_name", "city", "age"]