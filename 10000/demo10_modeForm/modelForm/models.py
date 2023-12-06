from django.db import models


# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30)