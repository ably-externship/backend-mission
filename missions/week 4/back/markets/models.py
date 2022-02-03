from django.db import models
from core import models as core_models


class Market(core_models.DateTimeModel):
    name = models.CharField(max_length=20, unique=True)
    owner = models.OneToOneField('accounts.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
