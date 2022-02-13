from django.contrib.auth.models import User
from django.db import models

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, null=True, max_length=20)
    address = models.CharField(blank=True, null=True, max_length=150)
    market = models.CharField(max_length=200, unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.market}"

    #seller 등록 후 저장할 때 user의 기존 is_staff 상태를 True로 변경
    def save(self, *args, **kwargs):
        user = self.user
        user.is_staff = True
        user.save()
        super(Seller, self).save(*args, **kwargs)
