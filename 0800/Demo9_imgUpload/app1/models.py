from django.db import models


# Create your models here.
class UploadImg(models.Model):
    img = models.FileField(upload_to="pic", null=True, default="")
    name = models.CharField(max_length=200, null=True)
