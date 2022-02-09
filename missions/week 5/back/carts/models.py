from django.db import models
from core import models as core_models


class Cart(core_models.DateTimeModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='carts')
    product_option = models.ForeignKey('products.ProductOption', on_delete=models.CASCADE, related_name='carts')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('user', 'product', 'product_option'),)

