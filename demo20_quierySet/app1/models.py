from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=50, default=None)
    date = models.DateField()
    
class Student(models.Model):
    
    passed = "Pass"
    Failed = "Fail"
    
    result = {
        (passed , "Pass"),
        (Failed , "Fail")
    }
    
    stu_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=50)
    result = models.CharField(max_length=50, choices=result)
    city = models.CharField(max_length=50, default=None)
    date = models.DateField()