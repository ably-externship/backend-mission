# Generated by Django 4.0.1 on 2022-02-13 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_market_site_url'),
        ('product', '0003_alter_productcategory_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='구매일')),
                ('product_num', models.PositiveIntegerField(default=0, verbose_name='구매수량')),
                ('per_price', models.PositiveIntegerField(default=0, verbose_name='개당가격')),
                ('is_delivered', models.BooleanField(default=False)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('is_refunded', models.BooleanField(default=False)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='market.market')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
                ('realproduct', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.realproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]