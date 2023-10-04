from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import * 

class ModifiedUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []