from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from base.settings.common import AUTH_USER_MODEL


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField('이름', max_length=100)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    profile_image = models.ImageField('프로필 이미지', blank=True, upload_to='accounts/profile_images/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=7)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    extra_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
