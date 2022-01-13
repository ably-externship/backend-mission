from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='상품명')
    price = models.CharField(max_length=100, verbose_name='가격')
    count = models.IntegerField(verbose_name='재고')
    description = models.TextField(max_length=200, verbose_name='설명')
    image = models.ImageField(upload_to='product/', null=True, verbose_name='사진')

    seller = models.CharField(max_length=200, null=True, verbose_name='입점사')

    def __str__(self):
        return f'<입점사:{self.seller}> {self.name}'


class ProductReal(models.Model):
    size = models.CharField(max_length=200, null=True, verbose_name='사이즈')
    color = models.CharField(max_length=100, null=True, verbose_name='색상')

    def __str__(self):
        return f'옵션: {self.size} , {self.color}'
