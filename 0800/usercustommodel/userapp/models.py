from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import UserManager
# Create your models here.


class CustomUser(AbstractUser):    
    username = None
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length = 100, unique = True)
    # cnfrm_passw = models.CharField(max_length=100, blank=True, null=True)
    is_parent = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
                