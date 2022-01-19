from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/question/", views.question, name="question"),
    path('search/', views.search, name='search'),

    # path('<int:pk>/cart-create/', views.cart_create, name="cart-create"),
    # path('cart-list/', views.CartListView.as_view(), name="cart-list")
]
