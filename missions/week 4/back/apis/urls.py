from django.urls import path, include
from .views import UserLoginView, UserCreateView, UserLogoutView, CommentCreateView, CartAddView, CartPlusView, \
    CartMinusView, CartDeleteView

# REST framework
from .api_product import ProductViewSet, CategoryView, BrandView, brands_list, brands_detail, BrandMasterView
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested.routers import NestedDefaultRouter

# 4주차
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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

# 4주차
brand_list = BrandMasterView.as_view({
    'get': 'list',
    'post': 'create',
})

brand_detail = BrandMasterView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

# router = SimpleRouter()
# router.register(r'', BrandMasterView)

# Product API urls
product_urlpatterns = [
    # 상품 목록
    path('', product_list, name='api_product_list'),
    # 상품 상세
    path('<int:pk>/', product_detail, name='api_product_detail'),
    # 카테고리 별 상품
    path('category/<int:pk>/', CategoryView.as_view(
        {'get': 'list'}
    ), name='api_category'),
    # 브랜드 별 상품
    # path('brand/<int:pk>/', brand_list, name='api_brand'),
    # path('brand_list/', brands_list, name='api_brand_list'),
    # path('brand_list/<int:pk>/', brands_detail),

    # 4주차
    # 브랜드 별 상품 url
    path('brand/', brand_list),
    path('brand/<int:pk>/', brand_detail),
]

# 4주차
# simple token url
token_urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    # 3주차
    # 상품 API 별로 분리를 하기 위함
    path('product/', include(product_urlpatterns)),

    # 4주차
    # path('brand/', include(router.urls)),

    # 4주차
    path('token/', include(token_urlpatterns)),

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
