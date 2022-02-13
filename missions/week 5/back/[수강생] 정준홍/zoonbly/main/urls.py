from unicodedata import category
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', home, name="home"),
    # 상품 추가 수정 삭제
    path('productNew/', productNew, name="productNew"),
    path('prodectCreate/', productCreate, name="productCreate"),
    path('productDetail/<int:id>', productDetail, name="productDetail"),
    path('productEdit/<int:id>', productEdit, name="productEdit"),
    path('productUpdate/<int:id>', productUpdate, name="productUpdate"),
    path('productDelete/<int:id>', productDelete, name="productDelete"),

    # 옵션 추가 수정 삭제
    path('opotionNew/<int:productId>', optionNew, name="optionNew"),
    path('optionCreate/<int:productId>', optionCreate, name="optionCreate"),
    path('optionEdit/<int:productId>/<int:optionId>', optionEdit, name="optionEdit"),
    path('optionUpdate/<int:productId>/<int:optionId>', optionUpdate, name="optionUpdate"),
    path('optionDelete/<int:productId>/<int:optionId>', optionDelete, name="optionDelete"),

    # 질문 추가 수정 삭제
    path('questionCreate/<int:productId>', questionCreate, name="questionCreate"),
    path('questionEdit/<int:productId>/<int:questionId>', questionEdit, name="questionEdit"),
    path('questionUpdate/<int:productId>/<int:questionId>', questionUpdate, name="questionUpdate"),
    path('questionDelete/<int:productId>/<int:questionId>', questionDelete, name="questionDelete"),

    # 답변 생성
    path('answerCreate/<int:productId>/<int:questionId>', answerCreate, name="answerCreate"),

    # 검색
    path('search/', search, name='search'),

    # 마켓별 상품 페이지
    path('marcket/<str:marcket>', marcket, name="marcket"),

    # 카테고리별 상품 페이지
    path('category/<str:category>', categoryPage, name="categoryPage"),
]