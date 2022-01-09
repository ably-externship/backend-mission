from django.db import models
from user.models import User
from product.models import Product


class Inquiry(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.CASCADE)
