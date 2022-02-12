from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from product.models import RealProduct

class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE) # 유저
    product = models.ForeignKey(RealProduct,on_delete=models.CASCADE) # 상품
    quantity = models.PositiveIntegerField(default = 0) # 개수
    reg_date = models.DateTimeField('등록일',auto_now_add=True)

    def total_price(self):
        return self.quantity*self.product.product.price


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING) # 상품 
    purchase_date = models.DateTimeField('구매일',auto_now_add=True)
    is_delivered = models.BooleanField(default = False)
    total_price = models.PositiveIntegerField(default = 0)
    is_refunded = models.BooleanField(default = False)

    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    cart = models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
    


