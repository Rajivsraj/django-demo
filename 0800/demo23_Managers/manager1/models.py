from django.db import models
from .managers import CustomManager


# Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=60)
#     city = models.CharField(max_length=60)
#     age = models.IntegerField()
#
#     # custom manger
#     myManger = models.Manager()
#     objects = models.Manager()



# class Student(models.Model):
#     name = models.CharField(max_length=60)
#     city = models.CharField(max_length=60)
#     age = models.IntegerField()
#
#     # custom manger
#     myCustomManger = CustomManager()
#     objects = models.Manager()
#     myManger = models.Manager()
#


class Student(models.Model):
    name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    age = models.IntegerField()

    # custom manger
    objects = models.Manager()
    myCustomManager = models.Manager()