from django.db import models

# Create your models here.
from markets.models import Market


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    original_price = models.BigIntegerField()
    discounted_price = models.BigIntegerField()

    detail = models.TextField()

    hidden = models.BooleanField(default=False)
    sold_out = models.BooleanField(default=False)

    hit_count = models.PositiveIntegerField(default=0)
    review_count = models.PositiveIntegerField(default=0)
    review_point = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    option1_type = models.CharField(max_length=10, default='SIZE')
    option1_name = models.CharField(max_length=50)
    option1_display_name = models.CharField(max_length=50)

    option2_type = models.CharField(max_length=10, default='COLOR')
    option2_name = models.CharField(max_length=50)
    option2_display_name = models.CharField(max_length=50)

    option3_type = models.CharField(max_length=10, default='', blank=True)
    option3_name = models.CharField(max_length=50, default='', blank=True)
    option3_display_name = models.CharField(max_length=50, default='', blank=True)

    hidden = models.BooleanField(default=False)
    sold_out = models.BooleanField(default=False)
    added_price = models.BigIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.product.discounted_price + self.added_price

    def __str__(self):
        return f'{self.option1_type} {self.option1_display_name},\n{self.option2_type} {self.option2_display_name},\n{self.option3_type} {self.option3_display_name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.filename
