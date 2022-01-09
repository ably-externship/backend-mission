from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ------------------------------------------------------------------
# TableName   : Product
# Description : 상품 테이블
# ------------------------------------------------------------------
class Product(models.Model):
    image = models.ImageField(null=True, upload_to="", blank=True)
    title = models.TextField()
    price = models.PositiveIntegerField()
    context = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title