# Generated by Django 4.0.1 on 2022-01-11 03:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_rename_userprofile_customerprofile_sellerprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerProfile',
            new_name='UserProfile',
        ),
        migrations.DeleteModel(
            name='SellerProfile',
        ),
    ]
