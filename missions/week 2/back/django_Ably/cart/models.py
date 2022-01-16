from django.db import models

# Create your models here.
class Cart(models.Model):
    auth_user = models.ForeignKey('accounts.AuthUser', models.DO_NOTHING)
    quantity = models.IntegerField()
    item_id_item = models.ForeignKey('markets.Item', models.DO_NOTHING, db_column='Item_id_Item')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'



# class Cartitem(models.Model):
#     quantity = models.IntegerField()
#     item_id_item = models.ForeignKey('markets.Item', models.DO_NOTHING, db_column='Item_id_Item')  # Field name made lowercase.
#     cart_id_cart = models.ForeignKey(Cart, models.DO_NOTHING, db_column='Cart_id_Cart')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CartItem'
    
#     def sub_total(self):
#         return self.item_id_item.price * self.quantity
    
#     def __str__(self):
#         return self.item_id_item