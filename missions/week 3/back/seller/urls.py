from django.urls import path
from .views import *

app_name = 'seller'

urlpatterns = [
    path('register', register, name='register'),
    path('upload', upload_product, name='upload_product'),
]
