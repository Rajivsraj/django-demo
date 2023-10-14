from django.contrib import admin
from .models import Student, Faculty, Husband, Wife, Parents, Child


# Register your models here.
@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    # class Meta:
    #     fields = "__all__"

    # def __str__(self):
    #     return
    list_display = ("h_name", "gender")
    # list_display = ["__all__"]


@admin.register(Wife)
class WifeAdmin(admin.ModelAdmin):
    list_display = ["w_name", "child_name"]
    # class Meta:
    #     fields = "__all__"


@admin.register(Parents)
class ParentsAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    class Meta:
        fields = "__all__"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "city", "phone", "salary", "fees")
    # list_display = [__all__]


@admin.register(Faculty)
class FaclutyAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "city", "phone", "salary", "qualification", "email")
    # list_display = ["__all__"]