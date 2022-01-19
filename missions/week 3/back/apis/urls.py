from django.urls import path, include
from .views import UserLoginView, UserCreateView, UserLogoutView, CommentCreateView, CartAddView, CartPlusView, \
    CartMinusView, CartDeleteView

# REST framework
from .api_product import ProductViewSet, CategoryView, BrandView


# 3주차
# 상품 리스트에서 읽기과 생성 가능
product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

# 상품 상세 화면에서 검색, 수정, 삭제가 가능
product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# Product API urls
post_urlpatterns = [
    path('', product_list, name='api_product_list'),
    path('<int:pk>/', product_detail, name='api_product_detail'),
    path('category/<int:pk>/', CategoryView.as_view(
        {'get': 'list'}
    ), name='api_category'),
    path('brand/<int:pk>/', BrandView.as_view(
        {'get': 'list'}
    ), name='api_brand'),

]


urlpatterns = [
    # 3주차
    # 상품 API 별로 분리를 하기 위함
    path('product/', include(post_urlpatterns)),

    # user api
    path('v1/user/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/user/logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
    path('v1/user/create/', UserCreateView.as_view(), name='apis_v1_user_create'),

    # cart api
    path('v1/cart/add/', CartAddView.as_view(), name='apis_v1_cart_add'),
    path('v1/cart/plus/', CartPlusView.as_view(), name='apis_v1_cart_plus'),
    path('v1/cart/minus/', CartMinusView.as_view(), name='apis_v1_cart_minus'),
    path('v1/cart/delete/', CartDeleteView.as_view(), name='apis_v1_cart_delete'),

    # comment api
    path('v1/comment/create/', CommentCreateView.as_view(), name='apis_v1_comment_create'),
]
