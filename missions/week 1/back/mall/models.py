from django.db import models

# Create your models here.



#여러 쇼핑몰 존재 

##카테고리
# class ShopCategory(models.Model):
#     category_name = models.CharField(max_length=20)

#쇼핑몰


class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    img_url = models.TextField()
    # category = models.ForeignKey(ShopCategory,  on_delete=models.CASCADE, verbose_name='쇼핑몰')  # 여러 카테고리
    category_name = models.CharField(max_length=20)

    #mall : 상품관리자 = 1 : N

    #

    def buy(self): #재고 부족시 동대문에서 사입
        print("동대문 사입") #얼마나 사야하나



