from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category_status = models.CharField(default="ACTIVE", max_length=13)
