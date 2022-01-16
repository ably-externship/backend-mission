from django.contrib.auth.models import User
from django.db import models
from shop.models import Market

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    market = models.OneToOneField(Market, on_delete=models.CASCADE, null=True, related_name='sellers')
    def __str__(self):
        return f"{self.user.username}, {self.market}"
