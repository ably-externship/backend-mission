from django.urls import path
from .views import ProductDetailView, index

app_name = 'mutbly'
urlpatterns = [
	path('', index, name="index"),
	path('detail/<int:pk>', ProductDetailView.as_view(), name="detail"),
]
