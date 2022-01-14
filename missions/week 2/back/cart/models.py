from django.db import models
from user.models import Account

# Cart table
class Cart(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
