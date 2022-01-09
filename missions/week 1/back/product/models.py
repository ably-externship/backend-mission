from django.db import models
from user.models import User
from shop.models import Shop


class Category(models.Model):
    category_id = models.CharField(max_length=10, primary_key=True)
    category_name = models.CharField(max_length=10)


class Product(models.Model):
    product_id = models.CharField(max_length=15, primary_key=True)
    product_name = models.CharField(max_length=30)
    product_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='None', db_column="category")
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column="shop_id")


class ProductDetail(models.Model):
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    main_image = models.ImageField(null=True, upload_to="", blank=True)
    detail_image = models.ImageField(null=True, upload_to="", blank=True)
    stock = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product_id")


class Board(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product_id")
    title = models.CharField(max_length=20, default='문의')
    content = models.CharField(max_length=200)
    comment = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="알 수 없음", db_column="user_id")
    secret = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, default=None)
    comment_date = models.DateTimeField(null=True, default=None)
