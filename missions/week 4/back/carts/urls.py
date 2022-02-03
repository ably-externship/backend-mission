from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('list/', views.CartListView.as_view(), name="list"),
    path('product/<int:product_id>/create/', views.cart_create, name="create"),
    path('<int:pk>/delete/', views.CartDeleteView.as_view(), name="delete"),
    path('<int:pk>/product/<int:product_id>/update/', views.cart_update, name="update")
]
