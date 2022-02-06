from django.db import models

# Create your models here.
from base.settings.common import AUTH_USER_MODEL


class Market(models.Model):
    name = models.CharField(max_length=255)
    site_url = models.URLField()
    email = models.EmailField()
    master = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
