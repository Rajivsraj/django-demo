from django.db import models

# Create your models here.

class StudentModel(models.Model):
    pic = models.FileField(upload_to="stu", max_length=250, null=True, default=None)
