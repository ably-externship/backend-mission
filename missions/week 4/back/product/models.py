from django.conf import settings
from django.db import models


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.PROTECT, related_name='author')
    name = models.CharField(max_length=200, verbose_name='상품명')
    seller = models.CharField(max_length=200, null=True, verbose_name='입점사')
    price = models.PositiveIntegerField(verbose_name='가격(원)')
    image = models.ImageField(upload_to='product/', null=True, verbose_name='사진')
    description = models.TextField(verbose_name='상품설명')

    def get_seller(self):
        return self.seller

    # def __str__(self):
    #     return f'{self.seller}::'


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productoption')
    size = models.CharField(max_length=100, verbose_name='사이즈')
    color = models.CharField(max_length=100, verbose_name='색상')
    stock_count = models.PositiveIntegerField(verbose_name='재고')

    def __str__(self):
        return f'{self.product_id}::{self.size}::{self.color}::{self.stock_count}'


class CartItem(models.Model):
    user = models.ForeignKey('local_account.User', on_delete=models.CASCADE, verbose_name='구매유저')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='구매상품')
    product_option = models.ForeignKey(ProductOption,
                                       on_delete=models.PROTECT, verbose_name='구매상품의 옵션')
    quantity = models.IntegerField(verbose_name='구매수량')

    def __str__(self):
        return f'{self.user_id}::{self.product_id}::{self.product_option_id}::{self.quantity}'


class Order(models.Model):
    user = models.ForeignKey('local_account.User', on_delete=models.CASCADE, verbose_name='구매유저')
    ordered_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user_id}::{self.ordered_date}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='구매상품')
    product_option = models.ForeignKey(ProductOption,
                                       on_delete=models.PROTECT, verbose_name='구매상품의 옵션')
    quantity = models.IntegerField(verbose_name='구매수량')

    def __str__(self):
        return f'{self.order_id}::{self.product_id}::{self.product_option_id}::{self.quantity}'
