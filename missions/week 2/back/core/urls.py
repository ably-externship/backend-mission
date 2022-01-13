from django.urls import path
from products import views as products_views

app_name = 'core'

urlpatterns = [
    path("", products_views.ProductListView.as_view(), name="home"),
]
