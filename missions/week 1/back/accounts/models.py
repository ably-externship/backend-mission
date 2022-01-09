from django.db import models

# Create your models here.
from mbly import settings


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=7)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    extra_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
