from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    seller = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    price = models.IntegerField()
    image = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'seller: {self.seller} | name: {self.name}'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author: {self.user} | content: {self.content}'
