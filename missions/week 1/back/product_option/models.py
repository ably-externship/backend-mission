from django.db import models

# Create your models here.
from product.models import Product


class ProductOption(models.Model):
    product_pk = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product_fk")
    size = models.FloatField
    color = models.CharField(max_length=10)
    sold_out_yn = models.BooleanField
    inventory_Count = models.IntegerField
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

