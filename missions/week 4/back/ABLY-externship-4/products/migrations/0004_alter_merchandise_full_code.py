# Generated by Django 3.2 on 2022-01-23 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220122_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='full_code',
            field=models.CharField(max_length=12, verbose_name='옵션상품 전체코드'),
        ),
    ]
