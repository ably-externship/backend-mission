from django.urls import include, path
from .views import CartAddView, CartClearView, CartUpdateView, CartDeleteView, CartDetailView


app_name = 'carts'

urlpatterns = [
    path('add/product/<int:pk>', CartAddView.as_view(), name='cart_add'),
    path('detail', CartDetailView.as_view(), name='cart_detail'),
    path('change/product/<int:pk>', CartUpdateView.as_view(), name='cart_delete'),
    path('exclude/product/<int:pk>', CartDeleteView.as_view(), name='cart_delete'),
    path('clear', CartClearView.as_view(), name='cart_clear'),
]