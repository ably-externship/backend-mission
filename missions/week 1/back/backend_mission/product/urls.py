from django.urls import path
from django.views.generic import TemplateView

from product.views import ProductCreateView, ProductDetailView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='product/list.html'), name='list'),
    path('create/',ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
]