from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Shop(models.Model):
    shop_id = models.CharField(max_length=10, primary_key=True)
    shop_name = models.CharField(max_length=20)
    shop_pw = models.CharField(max_length=20, null=True, default=None)
