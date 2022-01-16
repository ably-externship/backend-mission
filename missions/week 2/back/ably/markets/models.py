from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Market(models.Model):
    master = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.master.get_username()}: {self.name}'
