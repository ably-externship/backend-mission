from django.db import models
from user.models import User
from product.models import Product

# Product_qna table
class Product_qna(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=255, verbose_name='질문내용')
    datetime = models.DateTimeField(auto_now=True, verbose_name='작성일')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_feature',default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_feature',default="")

    def __str__(self):
        return self.content



