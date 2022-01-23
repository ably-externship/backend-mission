from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

from urllib.parse import urlparse
from django.core.files import File
from utils.file import download, get_buffer_ext

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])


class Market(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(null=False, allow_unicode=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField(blank=True, null=True)
    display = models.BooleanField('Display', default=True)
    detail = RichTextUploadingField()   # 편집기 스타일로 입력
    image = models.ImageField(blank=True, upload_to='images/')
    image_url = models.TextField(max_length=400, blank=True)
    def __str__(self):
        return self.name

    def save_slug(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class DetailImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/')

# class Color(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class Size(models.Model):
#     option = models.CharField(max_length=20)
#     def __str__(self):
#         return self.option


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    color = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, null=True)
    stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.product}, {self.color}, {self.size}, {self.stock}"

    class Meta:
        verbose_name = 'inventory'
        verbose_name_plural = 'inventories'


class Question(models.Model):
    title = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title