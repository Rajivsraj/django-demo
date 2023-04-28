from django.db import models
# Create your models here.


class StudentDetails(models.Model):
    fname = models.CharField(max_length=50, default=None, null=True)
    lname = models.CharField(max_length=50, default=None, null=True)
    password = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50, default=None, null=True)
    phone = models.CharField(max_length=50, default=None, null=True)