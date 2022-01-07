from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) #상품명
    writer = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    marcket = models.CharField(max_length=200) # 마켓명
    pub_date = models.DateTimeField() # 등록날짜
    price = models.IntegerField() # 가격
    description = models.TextField() #설명
    stock = models.IntegerField() #재고
    image = models.ImageField(upload_to = "product/", blank=True, null=True) # 상품 이미지