from django.db import models


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)