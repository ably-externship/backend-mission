from django.db import models
from user.models import User

# Cart table
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)