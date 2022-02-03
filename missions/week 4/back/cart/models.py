from django.db import models

# Create your models here.
from product_option.models import ProductOption
from users.models import User


class Cart(models.Model):
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_fk")
    product_option_fk = models.ForeignKey(ProductOption, on_delete=models.CASCADE, db_column="product_option_fk")
    quantity = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)