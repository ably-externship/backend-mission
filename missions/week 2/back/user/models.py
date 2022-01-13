from django.db import models

# User table
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128, verbose_name='아이디', default="")
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    email = models.CharField(max_length=128, verbose_name='이메일')
    # phone = models.CharField(max_length=128, verbose_name='핸드폰 번호')

