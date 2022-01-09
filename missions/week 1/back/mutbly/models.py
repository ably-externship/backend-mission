from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=100, verbose_name='상품명')
	price = models.IntegerField(verbose_name='판매가격')
	description = models.CharField(max_length=300, verbose_name='상품설명')
	stock = models.IntegerField(verbose_name='재고수량')
	add_date = models.DateField(auto_now_add=True, verbose_name='등록일')
	image = models.ImageField(upload_to='static/photos')


	def __str__(self):
		return self.name

	class Meta:
		db_table = 'mutbly_product'
		verbose_name = '상품'
		verbose_name_plural = '상품'

class User(models.Model):
	email = models.EmailField(verbose_name='E-mail')
	password = models.CharField(max_length=20, verbose_name='비밀번호')

	def __str__(self):
		return self.email

	class Meta:
		db_table = 'mutbly_user'
		verbose_name = '사용자'
		verbose_name_plural = '사용자'



