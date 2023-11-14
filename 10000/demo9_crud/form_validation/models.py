from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
