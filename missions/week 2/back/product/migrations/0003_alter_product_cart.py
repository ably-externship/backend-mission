# Generated by Django 4.0.1 on 2022-01-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_id_alter_cart_user'),
        ('product', '0002_alter_product_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='carts', to='cart.Cart'),
        ),
    ]
