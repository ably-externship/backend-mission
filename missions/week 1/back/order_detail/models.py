from django.db import models
from order.models import Order
from product.models import Product

# Order_detail table
class Order_detail(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField(verbose_name='가격')
    count = models.IntegerField(verbose_name='수량')

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.price



