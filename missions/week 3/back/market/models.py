from django.db import models

# Market 테이블
class Market(models.Model):
    id = models.AutoField(primary_key=True) # market_id
    name = models.CharField(max_length=128, verbose_name='업체명')  # 업체명
    admin = models.CharField(max_length=128, verbose_name='대표자 이름', default="") # 대표자 이름
    url = models.TextField(max_length=255, verbose_name='url' , default="") # 홈페이지 url
    email = models.TextField(max_length=255, verbose_name='이메일', default="") # 홈페이지 이메일
    reg_date = models.DateTimeField(auto_now=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='등록일')  # 갱신날짜
