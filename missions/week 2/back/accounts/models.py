from django.db import models

from core.models import TimeStampModel

class User(models.Model):
    email = models.CharField(max_length=100)
    is_social = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'

class UserInfo(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_information'

class SocialType(models.Model):
    social_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'social_type'

class SocialUserInfo(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_type = models.ForeignKey(SocialType, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'social_user_information'

class Seller(TimeStampModel):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    image_url = models.URLField(max_length=2000)
    phone_number = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

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