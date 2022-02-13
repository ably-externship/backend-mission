from itertools import product
from django.db import models
from product.models import Product,RealProduct
from market.models import Market
# Create your models here.



class ProductDailySales(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    sales = models.PositiveIntegerField(default = 0)
    sales_num = models.PositiveIntegerField(default = 0)
    
    class Meta:
        ordering = ('-date','-sales')


class MarketDailySales(models.Model):
    market =models.ForeignKey(Market,on_delete=models.DO_NOTHING)
    date = models.DateField()
    sales = models.PositiveIntegerField(default = 0)
    sales_num = models.PositiveIntegerField(default = 0)
    
    class Meta:
        ordering = ('-date','-sales')

