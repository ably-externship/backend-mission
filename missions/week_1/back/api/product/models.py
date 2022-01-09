from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'product'
        app_label = 'api.product'
        verbose_name = '상품'
        verbose_name_plural = '상품'

    def __str__(self):
        return self.name


