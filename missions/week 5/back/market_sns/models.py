from django.db import models

# Create your models here.
from market.models import Market


class MarketSns(models.Model):
    market_pk = models.ForeignKey(Market, on_delete=models.CASCADE, db_column="market_fk", related_name='market_sns')
    url = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


