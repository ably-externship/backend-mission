from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='생성날짜')
    updated = models.DateField(auto_now=True, verbose_name='업데이트날짜')
    
    class Meta:
        abstract = True