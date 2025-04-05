# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    is_paid_user = models.BooleanField(default=False)
