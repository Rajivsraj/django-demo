from django.db import models


# Create your models here.
class UploadImg(models.Model):
    name = models.CharField(max_length=22)
    img = models.FileField(upload_to="news/")
    # imag = models.ImageField(upload_to="im/", null=True, blank=True)

