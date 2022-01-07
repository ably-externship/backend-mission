from django.urls import path
from ..detail import views

app_name = 'detail'

urlpatterns = [
    path('<int:product_id>', views.get_product_view),
]