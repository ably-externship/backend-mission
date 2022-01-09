from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=128, verbose_name="이름", unique=True)
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    email = models.EmailField(verbose_name="이메일")

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email
