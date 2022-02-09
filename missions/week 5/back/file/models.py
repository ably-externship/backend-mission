from django.db import models

# Create your models here.
class File(models.Model):
    file_name = models.CharField(max_length=100)
    file_path = models.CharField(max_length=150)
    file_type = models.CharField(max_length=25)
    create_date = models.DateTimeField(auto_now_add=True)

