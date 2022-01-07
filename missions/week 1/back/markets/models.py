from django.db import models
from core import models as core_models


class Market(core_models.DateTimeModel):
    name = models.CharField(max_length=20, unique=True)
