from itertools import product
from django.db import models
from product.models import Product,RealProduct
# Create your models here.



class ProductDailySales(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    sales = models.PositiveIntegerField(default = 0)
    sales_num = models.PositiveIntegerField(default = 0)
    
    class Meta:
        ordering = ('-date','-sales')


class MarketDailySales(models.Model):
    date = models.DateField()
    sales = models.PositiveIntegerField(default = 0)
    sales_num = models.PositiveIntegerField(default = 0)
    
    class Meta:
        ordering = ('-date','-sales')

