from django.db import models


# Create your models here.
# table cration

class Student(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)


class Student1(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    age = models.IntegerField()
    phone = models.CharField(max_length=10, null=True, unique=True)


class Studetn2(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=60, null=True)
    city2 = models.CharField(max_length=50, blank=True)
    city3 = models.CharField(max_length=60, null=True, blank=True)

# insert into stu (name, city, city2, city3) values("rahul", "", "city2", "city3")