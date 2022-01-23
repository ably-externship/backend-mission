from django.db import models
from django.db.models.fields import CharField


class Vendor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return '{}'.format(self.name)
