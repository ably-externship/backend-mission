from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tmp_token = models.CharField(max_length=100, default=None, null=True)
