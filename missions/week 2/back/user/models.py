from django.db import models

# User table
class Account(models.Model):

    first_name = None
    last_name = None
    date_joined = None

    id = models.AutoField(primary_key=True) # user_id
    username = models.CharField(max_length=128, verbose_name='아이디', default="") # 아이디
    name = models.CharField(max_length=128, verbose_name='유저 이름', default="") # 유저 이름
    password = models.CharField(max_length=128, verbose_name='비밀번호') # 비밀번호
    email = models.CharField(max_length=128, verbose_name='이메일') # 이메일
    # phone = models.CharField(max_length=128, verbose_name='핸드폰 번호')

