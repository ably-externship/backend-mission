from django.urls import path
from . import views


urlpatterns = [
    # 제품 관련
    path('', views.ProductList, name="Productlist"),
    path('<int:pk>/', views.ProductDetail, name="ProductDetail"),
    path('create/', views.ProductCreate, name="ProductCreate"),
    path('update/<int:pk>/', views.ProductUpdate, name="ProductUpdate"),
    path('delete/<int:pk>/', views.ProductDelete, name="ProductDelete"),
    path('find/<str:name>/', views.ProductFind, name="ProductFind"),
    path('recommand/', views.ProductRecommandList, name="ProductRecommandlist"),

    # ElasticSearch
    path('search_by_elastic/', views.search_by_elastic, name='search_by_elastic'), # 테스트용

    # 옵션 관련
    path('option/', views.OptionList, name="OptionList"),
    path('option/create/', views.OptionCreate, name="OptionCreate"),
    # path('option/update/<int:pk>/', views.OptionUpdate, name="OptionUpdate"),
    # path('option/delete/<int:pk>/', views.OptionDelete, name="OptionDelete"),

    # 질문 관련
    path('qna/<int:pk>/', views.QnaList, name="QnaList"),
    path('qna/create/', views.QnaCreate, name="QnaCreate"),
]