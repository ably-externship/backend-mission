
from django.conf.urls.static import static
from django.urls import path

from base import settings
from product.views import ProductCreateView, ProductDetailView, ProductDeleteView, ProductListview

app_name = 'product'

urlpatterns = [
    path('list/', ProductListview.as_view(), name='list'),
    path('create/',ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)