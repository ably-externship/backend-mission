from tkinter import CASCADE
from django.db import models
from django.db.models.deletion import DO_NOTHING

from core.models import TimeStampModel
from accounts.models import Seller, User

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
    main_image_url = models.URLField(max_length=2000)
    colors = models.ManyToManyField(Color, through='ProductOption')
    sizes = models.ManyToManyField(Size, through='ProductOption')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'

class ProductHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_displayed = models.BooleanField(default=True)
    is_sold_out = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_histories'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'product_images'

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.IntegerField()
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_sold_out = models.BooleanField(default=False)

    class Meta:
        db_table = 'product_options'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'cart_items'

# view table
class ProductList(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=DO_NOTHING)
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=DO_NOTHING)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image_url = models.URLField(max_length=2000)
    seller_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'product_lists'

# view table
class CartItemList(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=DO_NOTHING)
    product_option = models.ForeignKey(ProductOption, on_delete=DO_NOTHING)
    product_name = models.CharField(max_length=100)
    main_image_url = models.URLField(max_length=2000)
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveSmallIntegerField()
    is_sold_out = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'cart_item_lists'