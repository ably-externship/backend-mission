from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_main, name='home'),
    path('category/<str:category_slug>', shop_main, name='product_in_category'),
    path('<int:product_id>/<product_slug>', product_detail, name='product_detail'),
    path('search', search, name='search'),
    #상품 문의
    path('question/<int:product_id>', question_create, name="question_create"),
    path('question-detail/<int:question_id>', question_detail, name="question_detail"),
    path('question-modify/<int:question_id>', question_modify, name="question_modify"),
    path('question-remove/<int:question_id>', question_delete, name="question_delete"),
]