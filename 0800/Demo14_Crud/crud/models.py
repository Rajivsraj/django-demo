from django.db import models


# Create your models here.
class StudentDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)


class AddStaff(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
