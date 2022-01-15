# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Board(models.Model):
#     title = models.CharField(max_length=20)
#     content = models.TextField()
#     writer = models.CharField(max_length=20)
#     id = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "board"


# class Product(models.Model):
#     name = models.CharField(max_length=20)
#     price = models.CharField(max_length=20)
#     color = models.CharField(max_length=20)
#     size = models.CharField(max_length=20)
#     description = models.CharField(max_length=200)
#     brand = models.CharField(max_length=40)
#     id = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = "product"


# class User(models.Model):
#     username = models.CharField(max_length=20)
#     id = models.CharField(primary_key=True, max_length=20)
#     password1 = models.CharField(max_length=20)
#     password2 = models.CharField(max_length=20)
#     email = models.CharField(max_length=50)

#     class Meta:
#         managed = False
#         db_table = "user"
