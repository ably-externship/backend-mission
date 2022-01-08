from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', home, name="home"),
    path('productNew/', productNew, name="productNew"),
    path('prodectCreate/', productCreate, name="productCreate"),
    path('productDetail/<int:id>', productDetail, name="productDetail"),
    path('productEdit/<int:id>', productEdit, name="productEdit"),
    path('productUpdate/<int:id>', productUpdate, name="productUpdate"),
    path('productDelete/<int:id>', productDelete, name="productDelete"),
    path('questionCreate/<int:productId>', questionCreate, name="questionCreate"),
    path('questionEdit/<int:productId>/<int:questionId>', questionEdit, name="questionEdit"),
    path('questionUpdate/<int:productId>/<int:questionId>', questionUpdate, name="questionUpdate"),
    path('questionDelete/<int:productId>/<int:questionId>', questionDelete, name="questionDelete"),
    path('answerCreate/<int:productId>/<int:questionId>', answerCreate, name="answerCreate"),
    path('search/', search, name='search'),
]