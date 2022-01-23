from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class LoginChoices(models.TextChoices):
        DEFAULT = "default"
        KAKAO = "kakao"

    register_login_method = models.CharField(max_length=10,
                                             blank=True,
                                             choices=LoginChoices.choices,
                                             default="default")
    # social_id = models.CharField(max_length=100, null=True)
