# Generated by Django 3.2 on 2022-01-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutbly', '0003_remove_quantity_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]