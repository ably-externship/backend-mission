# Generated by Django 3.2 on 2022-01-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220115_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phoneverification',
            options={'verbose_name_plural': '4. 휴대폰인증 목록'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
