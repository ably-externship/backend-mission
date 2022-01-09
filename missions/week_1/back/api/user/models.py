from django.db import models


class User(models.Model):
    id = models.CharField(verbose_name='아이디')
    user_id = models.CharField(verbose_name='아이디')
    name = models.CharField(verbose_name='이름')
    phone = models.IntegerField(verbose_name='핸드폰 번호')
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    updated_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'user'
        app_label = 'api.user'
        verbose_name = '고객'
        verbose_name_plural = '고객'

    def __str__(self):
        return self.user_id