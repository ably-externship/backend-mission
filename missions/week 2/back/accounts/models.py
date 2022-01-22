from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    first_name = None
    last_name = None
    date_joined = None

    reg_date = models.DateTimeField('등록날짜', auto_now_add=True)
    update_date = models.DateTimeField('갱신날짜', auto_now=True)

    name = models.CharField('이름', max_length=100)
    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    profile_img = models.ImageField('프로필이미지', blank=True, upload_to="accounts/profile_img/%Y/%m/%d",
                                    help_text="gif/png/jpg 이미지를 업로드해주세요.")

