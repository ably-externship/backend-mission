from django.db import models


# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(primary_key=True, max_length=20)
    brand_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand'


class Sangpum(models.Model):
    obj_name = models.CharField(max_length=14)
    obj_color = models.CharField(max_length=14)
    obj_size = models.CharField(max_length=4)
    brand_code = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    discount_price = models.CharField(max_length=20, blank=True, null=True)
    obj_code = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangpum'


class Type(models.Model):
    type_code = models.CharField(primary_key=True, max_length=4)
    type_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    pw = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    id_num = models.CharField(max_length=14, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)

    managed = False
    db_table = 'user'
