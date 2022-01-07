from django.db import models


# Create your models here.
from file.models import File
from market.models import Market


class Product(models.Model):
    market_pk = models.ForeignKey(Market, on_delete=models.CASCADE,  db_column="markey_fk")
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    sold_out_yn = models.BooleanField(default=False)
    descriptions = models.TextField(blank=True, default='')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    files = models.ManyToManyField(File)
