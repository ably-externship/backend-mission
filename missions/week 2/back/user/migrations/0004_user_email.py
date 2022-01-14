# Generated by Django 4.0.1 on 2022-01-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='이메일'),
            preserve_default=False,
        ),
    ]
