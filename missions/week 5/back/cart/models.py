from django.db import models
from user.models import User
# from product.models import Product

# Cart table
class Cart(models.Model):
    id = models.AutoField(primary_key=True) # cart_id

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart') # user_id
    product = models.ManyToManyField('product.Product', related_name='cart', blank=True)  # product_id   # circular import 발생
    product_option = models.ManyToManyField('product.Product_option', related_name='cart', blank=True) # product_option_id