from django.contrib.auth.models import User
from django.db import models
from user.models import Account

# Deliver table
class Deliver(models.Model):
    id = models.AutoField(primary_key=True) # product_review_id
    zipcode = models.TextField(max_length=255, verbose_name='우편번호') # 우편번호
    address = models.TextField(max_length=255, verbose_name='주소') # 주소
    adrress_detail = models.TextField(max_length=255, verbose_name='상세주소') # 상세주소

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='deliver') # user_id





