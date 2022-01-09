from django.urls import path

from . import views

app_name = 'goods'
urlpatterns = [
    # 쇼핑몰 상품 리스트
    path('', views.index, name='index'),
    # 검색
    path('search/', views.FormWithSearchView.as_view(), name='search'),
    # 쇼핑몰 상품 상세페이지
    path('<int:product_id>/', views.detail, name='detail'),
    # 상품질문기능
    path('question_create/<int:product_id>/', views.question_create, name='question_create'),
]