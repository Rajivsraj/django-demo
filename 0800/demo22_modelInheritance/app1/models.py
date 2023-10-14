from django.db import models


# Create your models here.
class Husband(models.Model):
    h_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)


class Wife(Husband):
    w_name = models.CharField(max_length=60)
    child_name = models.CharField(max_length=60)


class Parents(models.Model):
    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=20)
    salary = models.IntegerField()
    property = models.CharField(max_length=60)


class Child(Parents):
    school = models.CharField(max_length=100)
    cname = models.CharField(max_length=60)


class CommonClass(models.Model):
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    city = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    salary = models.IntegerField()

    class Meta:
        abstract = True


class Student(CommonClass):
    fees = models.IntegerField()
    salary = None


class Faculty(CommonClass):
    qualification = models.CharField(max_length=60)
    email = models.CharField(max_length=20)
