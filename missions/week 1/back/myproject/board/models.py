from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "board"
