from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/', null=True)
    quantity = models.IntegerField(default=0)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.reg_date)
