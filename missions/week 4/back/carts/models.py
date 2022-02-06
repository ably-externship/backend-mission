from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from base.settings.common import AUTH_USER_MODEL
from products.models import ProductOption


class Cart(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.product_option.get_price() * self.quantity

    def __str__(self):
        return f'{self.user.username} {self.product_option} {self.quantity}'
