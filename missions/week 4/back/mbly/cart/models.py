from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from product.models import RealProduct

class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE) # 유저
    product = models.ForeignKey(RealProduct,on_delete=models.CASCADE) # 상품
    quantity = models.PositiveIntegerField(default = 0) # 개수

    reg_date = models.DateTimeField('등록일',auto_now_add=True)

    def total_price(self):
        return self.quantity*self.product.product.price
