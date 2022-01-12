from django.db import models

# Seller table
class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name='업체명')

    def __str__(self):
        return self.name
