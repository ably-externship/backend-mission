from django.db import models

from core.models import TimeStampModel

class AccountType(models.Model):
    account_type = models.CharField(max_length=10)

    class Meta:
        db_table = 'account_type'

class SocialType(models.Model):
    social_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'social_type'

class Account(TimeStampModel):
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'accounts'

class User(models.Model):
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
    social_type = models.ForeignKey(SocialType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=15, null=True)

    class Meta:
        db_table = 'users'

class Seller(models.Model):
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    image_url = models.URLField(max_length=2000)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = 'sellers'

class FittingModel(TimeStampModel):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    height = models.PositiveSmallIntegerField()
    top_size = models.PositiveSmallIntegerField()
    bottom_size = models.PositiveSmallIntegerField()
    shoe_size = models.PositiveSmallIntegerField()
    image_url = models.URLField(max_length=2000)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'fitting_models'