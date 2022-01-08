from django.urls import path
from .views import ProductDetailView, index, detail

app_name = 'mutbly'
urlpatterns = [
	path('', index, name="index"),
	# path('detail/<int:product_id>', ProductDetailView.as_view(), name="detail"),
	path('detail/<int:product_id>', detail, name='detail')
]
