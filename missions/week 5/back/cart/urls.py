from django.urls import path
from . import views


urlpatterns = [
    # 장바구니 관련
    path('', views.CartList, name="CartList"),
    path('create/', views.CartCreate, name="CartCreate"),
    path('update/<int:pk>/', views.CartUpdate, name="CartUpdate"),
    path('delete/<int:pk>/', views.CartDelete, name="CartDelete"),
    # path('find/<str:name>/', views.ProductFind, name="ProductFind"),
]