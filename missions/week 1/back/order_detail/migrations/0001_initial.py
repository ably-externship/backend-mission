# Generated by Django 4.0.1 on 2022-01-06 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0002_rename_user_id_order_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField(verbose_name='가격')),
                ('count', models.IntegerField(verbose_name='수량')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.product')),
            ],
        ),
    ]