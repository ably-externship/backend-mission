# Generated by Django 4.0.1 on 2022-01-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productoption_extra_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='is_main',
        ),
        migrations.AddField(
            model_name='product',
            name='main_image_url',
            field=models.URLField(max_length=2000, null=True),
        ),
    ]