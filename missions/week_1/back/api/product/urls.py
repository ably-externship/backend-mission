from django.urls import path, include
from missions.week_1.back.api.product import views

app_name = 'product'

urlpatterns = [
    path('list', views.get_products),
    path('search/', views.ProductSearchView.as_view()),
    path('detail/', include('api.product.detail.urls', 'detail'))
]