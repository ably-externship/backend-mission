from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marcket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) #상품명
    user = models.ForeignKey(User, on_delete=models.CASCADE) #관리자

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) #상품명
    user = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    marcket = models.ForeignKey(Marcket, on_delete=models.CASCADE, max_length=50) # 마켓명
    pub_date = models.DateTimeField(auto_now=True) # 등록날짜
    description = models.TextField() #설명

class Option(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=50) # 마켓명
    user = models.ForeignKey(User, on_delete=models.CASCADE) #작성자
    pub_date = models.DateTimeField(auto_now=True) # 등록날짜
    color = models.CharField(max_length=50) #색상
    size = models.CharField(max_length=50) #사이즈
    stock = models.PositiveIntegerField() #재고
    price = models.PositiveIntegerField() #가격