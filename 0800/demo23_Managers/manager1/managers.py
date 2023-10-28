from django.db import models
# from .models import Student


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

