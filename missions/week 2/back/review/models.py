from django.db import models
from user.models import Account
from product.models import Product

# Product_review table
class Product_review(models.Model):
    id = models.AutoField(primary_key=True) # product_review_id
    title= models.CharField(max_length=128, verbose_name='리뷰제목', default="") # 제목
    content = models.TextField(max_length=255, verbose_name='리뷰내용') # 내용
    image = models.ImageField(upload_to='', null=True)  # 이미지
    point = models.IntegerField(verbose_name='평점') # 평점
    reg_date = models.DateTimeField(auto_now=True, verbose_name='등록일') # 등록날짜
    update_date = models.DateTimeField(auto_now=True, verbose_name='등록일')  # 갱신날짜

    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='product_review') # user_id
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review') # product_id

