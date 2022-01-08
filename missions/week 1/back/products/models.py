from django.db import models
from django.urls import reverse

from core import models as core_models


class Product(core_models.DateTimeModel):
    COLOR_CHOICES = (
        ('white', '흰색'),
        ('black', '검정색'),
        ('red', '빨간색'),
        ('green', '초록색'),
        ('blue', '파란색'),
    )
    SIZE_CHOICES = (
        ('s', 'SMALL'),
        ('m', 'MEDIUM'),
        ('l', 'LARGE'),
    )
    CATEGORY_CHOICES = (
        ('neat', '니트'),
        ('hood', '후드'),
        ('mtm', '맨투맨'),
        ('shirt', '셔츠'),
    )
    market = models.ForeignKey('markets.Market', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    stock = models.PositiveIntegerField(default=1)  # 재고

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.pk})


class Question(core_models.DateTimeModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='questions')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='questions')
    content = models.TextField()

    def __str__(self):
        return f'{self.user.email}, {self.product.name}, {self.content}'

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"pk": self.product_id})
