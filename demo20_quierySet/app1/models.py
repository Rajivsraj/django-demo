from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=50, default=None)