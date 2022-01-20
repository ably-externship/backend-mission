from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Market(models.Model):
    reg_date = models.DateTimeField('등록날짜',auto_now_add=True)
    update_date = models.DateTimeField('변경날짜',auto_now_add=True)
    name = models.CharField('이름',max_length=50)
    site_url=models.URLField('마켓 URL',max_length=150)
    master = models.OneToOneField(User,on_delete=models.CASCADE) # 대표


