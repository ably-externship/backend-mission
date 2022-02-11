# Generated by Django 3.2 on 2022-02-11 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_recommand',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='age_range',
            field=models.CharField(max_length=100, null=True, verbose_name='연령대'),
        ),
        migrations.AlterField(
            model_name='user_recommand',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_recommand', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
