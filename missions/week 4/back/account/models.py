from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    tmp_token = models.CharField(max_length=100, default=None, null=True)
    seller = models.CharField(max_length=100, null=True)


# class Seller(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller') # 역참조 가능?
#     seller = models.CharField(max_length=100)
#     is_staff = models.BooleanField(default=True, null=True)
#
#     class Meta:
#         db_table = 'seller'
