from django.db import models
from django.db.models import Manager


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='상품명')
    price = models.IntegerField(verbose_name='가격')
    size = models.CharField(max_length=200, null=True, verbose_name='사이즈')
    count = models.IntegerField(verbose_name='재고')
    description = models.TextField(max_length=200, verbose_name='설명')
    image = models.ImageField(upload_to='product/', null=True, verbose_name='사진')

    seller = models.CharField(max_length=200, null=True, verbose_name='입점사')

    objects = Manager()
