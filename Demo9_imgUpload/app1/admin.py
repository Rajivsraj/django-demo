from django.contrib import admin
from .models import UploadImg


# Register your models here.
@admin.register(UploadImg)
class UploadImgAdmin(admin.ModelAdmin):
    list_display = ["img", "name"]
