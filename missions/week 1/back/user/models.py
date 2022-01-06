from django.db import models

# User table
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=128, verbose_name='이메일')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    phone = models.CharField(max_length=128, verbose_name='핸드폰 번호')

    def __str__(self):
        return self.email