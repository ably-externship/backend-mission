from django.urls import include, path
from .views import MerchandiseDetail


app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>', MerchandiseDetail.as_view(), name='product_detail'),
]