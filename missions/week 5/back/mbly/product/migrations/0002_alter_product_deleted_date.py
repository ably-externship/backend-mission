# Generated by Django 4.0.1 on 2022-01-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='삭제날짜'),
        ),
    ]
