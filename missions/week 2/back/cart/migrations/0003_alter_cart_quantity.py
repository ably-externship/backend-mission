# Generated by Django 4.0.1 on 2022-01-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_created_at_alter_cart_inventory_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]