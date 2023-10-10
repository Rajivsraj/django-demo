from django.db import models


# Create your models here.
class Staff(models.Model):
    f_name = models.CharField(max_length=50, db_column="fname", null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    dept = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField()