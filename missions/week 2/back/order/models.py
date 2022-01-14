from django.db import models
from user.models import User
from product.models import Product


# Order table
class Order(models.Model):
    id = models.AutoField(primary_key=True)  # order_id
    datetime = models.DateTimeField(auto_now=True, verbose_name='주문시간')  # 주문시간
    status = models.CharField(max_length=128, verbose_name='주문상태')  # 주문상태

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')  # user_id


# Order_detail table
class Order_detail(models.Model):
    id = models.AutoField(primary_key=True)  # order_detail_id
    price = models.IntegerField(verbose_name='가격')  # 가격
    count = models.IntegerField(verbose_name='수량')  # 수량

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_detail')  # order_id
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_detail')  # product_id