from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"

    GENDER = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Others")
    ]
    city = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER, default=MALE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    course_name = models.CharField(max_length=40)
    duration = models.CharField(max_length=40)
    fees = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Roles(models.Model):
    role_name = models.CharField(max_length=40)
    user = models.ManyToManyField(User)


