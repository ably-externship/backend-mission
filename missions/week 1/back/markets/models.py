from django.db import models

# Create your models here.
from mbly import settings


class Market(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    original_price = models.BigIntegerField()
    discounted_price = models.BigIntegerField()
    detail = models.TextField()

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=7)
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.color} {self.size}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.filename


class ProductQuestion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    private = models.BooleanField(default=False)
    question = models.TextField()
    answer = models.TextField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
