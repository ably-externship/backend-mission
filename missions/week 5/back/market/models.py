from django.db import models
from user.models import User

# Market 테이블
class Market(models.Model):
    id = models.AutoField(primary_key=True) # market_id
    name = models.CharField(max_length=128, verbose_name='업체명')  # 업체명
    url = models.TextField(max_length=255, verbose_name='url', default="") # 홈페이지 url
    email = models.TextField(max_length=255, verbose_name='이메일', default="") # 홈페이지 이메일
    reg_date = models.DateTimeField(auto_now=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='등록일')  # 갱신날짜

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='market')  # user_id