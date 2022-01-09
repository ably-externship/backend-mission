from django.contrib import admin
from accounts.models import User
from products.models import MainCategory, SubCategory, Merchandise, Question, Comment

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'password',
        'email',
        'is_seller',
        'brand',
        'is_active',
        'is_staff',
        'is_admin',
        'is_superuser',
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


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    raw_id_fields = ('seller', 'subcategory')
    
    list_display = [
        'id',
        'subcategory',
        'seller',
        'common_code',
        'full_code',
        'name',
        'color',
        'size',
        'current_stock',
        'safety_stock',
        'soldout_state',
        'on_sale',
        'on_display',
        'standard_price',
        'discounted_price',
        'main_img',
        'sub_img_0',
        'sub_img_1',
        'sub_img_2',
        'created',
        'updated',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'merchandise')
    
    list_display = [
        'id',
        'user',
        'merchandise',
        'title',
        'content',
        'created',
        'updated',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('question', 'merchandise')
    
    list_display = [
        'id',
        'question',
        'merchandise',
        'content',
        'created',
        'updated',
    ]