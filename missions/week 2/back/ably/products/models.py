from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from markets.models import Market


# Create your models here.
class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.get_username()}: {self.content}'


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
