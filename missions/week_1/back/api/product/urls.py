from django.urls import path
from missions.week_1.back.api.product import views

app_name = 'product'

urlpatterns = [
    path('list', views.get_products_view),
    path('search', views.search_products_view),
    path('detail/<int:id>', views.product_detail)
]