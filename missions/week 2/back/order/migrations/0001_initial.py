# Generated by Django 4.0.1 on 2022-01-06 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='주문시간')),
                ('status', models.CharField(max_length=128, verbose_name='주문상태')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.user')),
            ],
        ),
    ]
