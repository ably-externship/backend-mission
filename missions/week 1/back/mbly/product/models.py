from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150) # 이름
    price = models.IntegerField() # 가격
    stock = models.IntegerField() # 재고
    description = models.CharField(max_length=200) # 설명
    image = models.ImageField(upload_to='images/') # 이미지
    registration_date = models.DateTimeField(auto_now=True) # 등록일

    class Meta:
        ordering = ['-registration_date'] # 역순 정렬


class Question(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date'] # 역순 정렬

class Answer(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date'] # 역순 정렬