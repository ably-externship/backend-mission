from django.db import models
from user.models import Account
from product.models import Product

# Product_qna table
class Product_qna(models.Model):
    id = models.AutoField(primary_key=True) # product_qna_id
    title= models.CharField(max_length=128, verbose_name='질문제목', default="") # 제목
    content = models.TextField(max_length=255, verbose_name='질문내용') # 내용
    reg_date = models.DateTimeField(auto_now=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='등록일')  # 갱신날짜

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='product_qna') # user_id
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_qna') # product_id




