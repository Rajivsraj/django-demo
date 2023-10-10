from django.contrib import admin
from .models import UploadImg


@admin.register(UploadImg)
# Register your models here.
class ImgAdmin(admin.ModelAdmin):
    list_display = ["name", "img"]