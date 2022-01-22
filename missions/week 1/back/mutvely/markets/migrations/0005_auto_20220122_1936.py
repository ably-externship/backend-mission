# Generated by Django 3.2.11 on 2022-01-22 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_product_productcategoryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='갱신날짜')),
                ('name', models.CharField(max_length=100, verbose_name='마켓이름')),
                ('site_url', models.URLField(max_length=100, verbose_name='마켓사이트URL')),
                ('email', models.EmailField(max_length=100, verbose_name='마켓대표이메일')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='markets.market'),
        ),
        migrations.DeleteModel(
            name='Markets',
        ),
    ]
