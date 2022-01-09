from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User

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


    def __str__(self):
        return self.name

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
    detail = RichTextUploadingField()   # 편집기 스타일로 입력
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Size(models.Model):
    option = models.CharField(max_length=20)
    def __str__(self):
        return self.option


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    stock = models.PositiveIntegerField()

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
        return self.comment