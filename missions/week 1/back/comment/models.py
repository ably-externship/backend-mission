
from django.db import models
from account.models import User
from product.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='comment', verbose_name='상품')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment', verbose_name='작성자')

    content = models.TextField(null=False)

    created_at = models.DateField(auto_now=True)

