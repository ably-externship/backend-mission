# Generated by Django 4.0.1 on 2022-01-07 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]