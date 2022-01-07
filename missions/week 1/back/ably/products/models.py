from django.db import models

from core.models import TimeStampModel
from accounts.models import Seller

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'product_categories'

class ProductSubcategory(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'product_subcategories'

class Color(models.Model):
    color = models.CharField(max_length=10)

    class Meta:
        db_table = 'colors'

class Size(models.Model):
    size = models.CharField(max_length=5)

    class Meta:
        db_table = 'sizes'

class Product(models.Model):
    product_subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    colors = models.ManyToManyField(Color, through='ProductOption')
    sizes = models.ManyToManyField(Size, through='ProductOption')

    class Meta:
        db_table = 'products'

class ProductHistory(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_displayed = models.BooleanField(default=True)
    is_sold_out = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_histories'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_images'

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.IntegerField()
    extra_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold_out = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_options'