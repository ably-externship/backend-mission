from django.db import models
from shop.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    violation = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ReviewBot(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    use_bot = models.BooleanField(default=False)
    def __str__(self):
         return self.user.username