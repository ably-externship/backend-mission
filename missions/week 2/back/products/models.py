from django.db import models
from django.urls import reverse

from core import models as core_models


class Product(core_models.DateTimeModel):
    market = models.ForeignKey('markets.Market', on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)

    is_sold_out = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})


class ProductOption(core_models.DateTimeModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='options')
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    stock = models.PositiveIntegerField(default=1)  # 재고
    add_price = models.IntegerField(default=0)
    is_sold_out = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Question(core_models.DateTimeModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='questions')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='questions')
    content = models.TextField()

    def __str__(self):
        return f'{self.user.email}, {self.product.name}, {self.content}'

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.product_id})
