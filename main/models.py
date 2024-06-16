from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
import re


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

