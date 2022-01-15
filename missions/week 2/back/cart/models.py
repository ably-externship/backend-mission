from django.db import models
from user.models import Account


# # Cart table
# class Cart(models.Model):
#     user = models.OneToOneField('user.Account',on_delete=models.CASCADE,primary_key=True) # cart_id
#
#     product = models.ManyToManyField('product.Product', related_name='cart', blank=True, null=True)  # product_id
