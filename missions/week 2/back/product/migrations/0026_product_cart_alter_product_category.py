# Generated by Django 4.0.1 on 2022-01-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_cart_product'),
        ('product', '0025_remove_product_cart_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='product', to='cart.Cart'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('트레이닝', '트레이닝'), ('스커트', '스커트'), ('기타', '기타'), ('주얼리', '주얼리'), ('가방', '가방'), ('패션소품', '패션소품'), ('신발', '신발'), ('언더웨어', '언더웨어'), ('팬츠', '팬츠'), ('아우터', '아우터'), ('원피스/세트', '원피스/세트'), ('상의', '상의')], default='아우터', max_length=80),
        ),
    ]
