from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255, default='')
    type = models.CharField(max_length=15 , default='')
    content = models.TextField(null=True)
    private_yn = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

