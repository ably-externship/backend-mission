from asyncio.windows_events import NULL
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from main.models import *

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # 사용자
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 상품
    amount = models.PositiveIntegerField(null=True)     # 수량