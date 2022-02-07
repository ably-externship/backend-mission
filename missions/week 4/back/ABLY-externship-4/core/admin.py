from django.contrib import admin
from accounts.models import User, Customer, Seller, PhoneVerification
from products.models import MainCategory, SubCategory, BaseMerchandise, Merchandise
from qna.models import Question, Answer


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'password',
        'email',
        'is_active',
        'is_staff',
        'is_admin',
        'is_superuser',
        'created',
        'updated',
    ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    
    list_display = [
        'id',
        'user',
        'phone_number',
        'is_local',
        'connect_social',
        'social_type',
        'social_id',
        'created',
        'updated',
    ]


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    
    list_display = [
        'id',
        'user',
        'phone_number',
        'brand',
        'created',
        'updated',
    ]


@admin.register(PhoneVerification)
class PhoneVerificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'phone_number',
        'verification_code',
        'is_verified',
        'is_used',
        'created',
        'updated',
    ]


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created',
        'updated',
    ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    raw_id_fields = ('maincategory',)
    
    list_display = [
        'id',
        'maincategory',
        'name',
        'created',
        'updated',
    ]


@admin.register(BaseMerchandise)
class BaseMerchandiseAdmin(admin.ModelAdmin):
    raw_id_fields = ('subcategory', 'seller')
    
    list_display = [
        'id',
        'subcategory',
        'seller',
        'common_code',
        'name',
        'standard_price',
        'discounted_price',
        'main_img',
        'sub_img_0',
        'sub_img_1',
        'sub_img_2',
    ]


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    raw_id_fields = ('basemerchandise',)
    
    list_display = [
        'id',
        'basemerchandise',
        'full_code',
        'color',
        'size',
        'current_stock',
        'safety_stock',
        'soldout_state',
        'on_sale',
        'on_display',
        'created',
        'updated',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields = ('customer', 'basemerchandise')
    
    list_display = [
        'id',
        'customer',
        'basemerchandise',
        'title',
        'content',
        'created',
        'updated',
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    raw_id_fields = ('question', 'basemerchandise')
    
    list_display = [
        'id',
        'question',
        'basemerchandise',
        'content',
        'created',
        'updated',
    ]