from django.db import models
from django.db.models.fields import CharField


class Vendor(models.Model):
    name = models.CharField(max_length=128)
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name="상품")

    def __str__(self):
        return '{} {}'.format(self.name)
