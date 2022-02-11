from django.db import models

# Create your models here.
from users.models import User


class Market(models.Model):
    company_name = models.CharField(max_length=12, unique=True)
    contact_number = models.CharField(max_length=13)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_fk", default=None, null=True)

    def __str__(self):
        return self.company_name