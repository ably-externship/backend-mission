from operator import mod
from django.db import models
from mutbly.models import Item, Quantity
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#### 문서보면서, cart html, model views 짜주는 중

class InCartItem(models.Model) :
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, related_name='cart')
  quantity = models.IntegerField()
  # total_price = models.IntegerField(null=True)
  active = models.BooleanField(default=True)
  created_at = models.DateTimeField(default=timezone.now)
  
  def itemTotalPrice(self) :
    return self.item.price * self.quantity.quantity
  

  
  
  