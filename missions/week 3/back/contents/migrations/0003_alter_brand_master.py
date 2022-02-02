# Generated by Django 4.0.1 on 2022-02-02 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0002_brand_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='master',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
