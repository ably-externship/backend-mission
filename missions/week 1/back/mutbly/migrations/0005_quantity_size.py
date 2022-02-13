# Generated by Django 3.2 on 2022-01-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutbly', '0004_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default=1, max_length=2),
        ),
    ]