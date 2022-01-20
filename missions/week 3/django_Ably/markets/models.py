from django.db import models

class Item(models.Model):
    id_item = models.CharField(db_column='id_Item', primary_key=True, max_length=5)  # Field name made lowercase.
    color = models.CharField(max_length=45, blank=True, null=True)
    size = models.CharField(max_length=45, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    store_id_store = models.ForeignKey('Store', models.DO_NOTHING, db_column='Store_id_Store')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'

class Store(models.Model):
    id_store = models.CharField(db_column='id_Store', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(max_length=45, blank=True, null=True)
    detail = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Store'