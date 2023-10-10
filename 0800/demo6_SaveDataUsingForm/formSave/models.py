from django.db import models


# Create your models here.
class Students(models.Model):
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    password = models.CharField(max_length=60)