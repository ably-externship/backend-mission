# Generated by Django 4.0.1 on 2022-01-22 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_category_product_category_fk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.CharField(default='ACTIVE', max_length=10),
        ),
    ]
