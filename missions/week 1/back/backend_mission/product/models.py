from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    size = models.CharField(max_length=200, null=True)
    count = models.IntegerField()
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='product/', null=False)

    seller = models.CharField(max_length=200, null=True)
    register = models.DateField(auto_now=True, null=True)
