# Generated by Django 4.0.1 on 2022-01-07 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=128, verbose_name='업체명'),
        ),
    ]