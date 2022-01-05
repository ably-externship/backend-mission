from django.db import models

# Create your models here.
class Market(models.Model):
    company_name = models.CharField(max_length=12, unique=True)
    contact_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name