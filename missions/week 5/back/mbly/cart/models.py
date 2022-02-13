from operator import mod
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from product.models import RealProduct,Product
from market.models import Market
class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE) # 유저
    product = models.ForeignKey(RealProduct,on_delete=models.CASCADE) # 상품
    quantity = models.PositiveIntegerField(default = 0) # 개수
    reg_date = models.DateTimeField('등록일',auto_now_add=True)

    def total_price(self):
        return self.quantity*self.product.product.price


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING) # 유저
    market = models.ForeignKey(Market,on_delete=models.DO_NOTHING) # 마켓
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    realproduct = models.ForeignKey(RealProduct,on_delete=models.DO_NOTHING)

    purchase_date = models.DateTimeField('구매일',auto_now_add=True)

    product_num = models.PositiveIntegerField('구매수량',default = 0)
    per_price = models.PositiveIntegerField('개당가격',default = 0)
    total_price = models.PositiveIntegerField('총 가격',default = 0)

    is_delivered = models.BooleanField(default = False)
    total_price = models.PositiveIntegerField(default = 0)
    is_refunded = models.BooleanField(default = False)
    is_checked = models.BooleanField(default = False)

    

# class OrderDetail(models.Model):
#     order = models.ForeignKey(Order,on_delete=models.DO_NOTHING)
#     cart = models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
    


