# Generated by Django 4.0.1 on 2022-02-11 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_refreshstorage_refresh_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='market_id',
        ),
    ]
