from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50, blank=True)
    salary = models.IntegerField(null=True)
    city = models.CharField(max_length=50, default=None)
    date = models.DateField(auto_now=True)
    
class Employee2(models.Model):
    
    # passed = "Pass"
    # Failed = "Fail"
    
    # result = {
    #     (passed , "Pass"),
    #     (Failed , "Fail")
    # }
    
    emp_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    salary = models.IntegerField(null=True)
    city = models.CharField(max_length=50, default=None)
    date = models.DateField(auto_now=True)
