from asyncio.windows_events import NULL
from pyexpat import model
from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from main.models import *

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 사용자
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품
    option = models.ForeignKey(Options, on_delete=models.CASCADE) # 옵션
    amount = models.PositiveIntegerField(null=True)     # 수량
    optionPrice = models.PositiveIntegerField(null=True) # 각 담은 상품 금액

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 사용자
    pur_date = models.DateTimeField(auto_now=True) # 구매날짜
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품
    option = models.ForeignKey(Options, on_delete=models.CASCADE) # 옵션
    amount = models.PositiveIntegerField(null=True)     # 수량
    totalPrice = models.PositiveIntegerField(null=True) # 결제 금액
    status = models.CharField(max_length=20)