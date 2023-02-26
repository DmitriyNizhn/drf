from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Users(AbstractBaseUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
