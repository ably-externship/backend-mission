from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    id = models.CharField(primary_key=True, max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "user"
