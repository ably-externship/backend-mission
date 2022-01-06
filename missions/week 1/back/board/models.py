from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=15)
    content = models.TextField
    private_yn = models.BooleanField
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

