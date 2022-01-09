from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', shop_main, name='home'),
    path('category/<str:category_slug>', shop_main, name='product_in_category'),
    path('<int:product_id>/<product_slug>', product_detail, name='product_detail'),
    path('search', search, name='search'),
    path('question/<int:question_id>', question_delete, name="question_delete"),
]
