from django.db import models
from seller.models import Seller
from cart.models import Cart

# Product table
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name='제품명')
    price = models.IntegerField(verbose_name='가격', default=0)
    count = models.IntegerField(verbose_name='재고')
    description = models.TextField(max_length=255, verbose_name='제품설명')
    register = models.DateTimeField(auto_now=True, verbose_name='등록일')
    size = models.CharField(max_length=128, verbose_name='사이즈')

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='sellers')  # related_name으로 역참조 가능
    cart = models.ManyToManyField(Cart,related_name='carts',blank=True,null=True)

    def __str__(self):
        return self.name
