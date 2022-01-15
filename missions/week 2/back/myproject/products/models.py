from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=40)
    id = models.CharField(primary_key=True, max_length=20)
    product_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "product"
