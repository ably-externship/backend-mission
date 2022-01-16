from django.db import models


class Shop(models.Model):
    shop_id = models.CharField(max_length=10, primary_key=True)
    shop_name = models.CharField(max_length=20)