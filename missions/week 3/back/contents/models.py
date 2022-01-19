from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


# BaseModel
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Brand Model
class Brand(models.Model):
    name = models.CharField(unique=True, max_length=100)
    brand_thumb = models.URLField('url', unique=True, null=True, blank=True)

    # 브랜드 url
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self):
        return self.name

    # brand url
    def get_absolute_url(self):
        return f'/product/brand/{self.slug}'


# Category Model
class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)

    # 카테고리 url
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, null=True, blank=True)

    def __str__(self):
        return self.name

    # category url
    def get_absolute_url(self):
        return f'/product/category/{self.slug}/'


# product Model
class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_img = models.URLField('url', unique=True, null=True, blank=True)
    # size

    # Category, Brand, Image Model 상속
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='product_category')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, related_name='product_brand')

    def __str__(self):
        return self.name

    # product url
    def get_absolute_url(self):
        return f'/product/{self.pk}/'


# Image Model
class Image(models.Model):
    image = models.URLField('url', unique=True, null=True, blank=True)

    # product Model 상속
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='image_product')


# Comment Model
class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='comment_product')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return '{} : {} ({})'.format(self.author, self.content, self.product)


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return '{} - {}'.format(self.product.name, self.user.username)

    def price_total(self):
        return self.product.price * self.quantity




