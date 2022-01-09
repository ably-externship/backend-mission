

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Item(models.Model):
  name = models.CharField(max_length=256)
  photo = models.ImageField(upload_to="image")
  price = models.IntegerField(default=0)
  description = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  
  def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

  def __str__(self):
      return self.name
    
    
    
class Quantity (models.Model):
  ITEM_SIZE = [
    ('XS', 'XS'), 
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'), 
  ]
  
  item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, related_name='quantities')
  size = models.CharField(max_length=2, choices=ITEM_SIZE, default="XS")
  color = models.CharField(max_length=256)
  quantity = models.IntegerField()

  
  def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()


class Question (models.Model):
  item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, related_name='questions')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  
  def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

