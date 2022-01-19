from django.urls import path, include
from .views import UserLoginView, UserCreateView, UserLogoutView, CommentCreateView, CartAddView, CartPlusView, \
    CartMinusView, CartDeleteView

# REST framework
from .api_product import ProductViewSet, CategoryView, BrandView
from .api_product import post_list, post_detail

post_urlpatterns = [
    path('', post_list, name='api_product_list'),
    path('<int:pk>/', post_detail, name='api_product_detail'),
    path('category/<int:pk>/', CategoryView.as_view(
        {'get': 'list'}
    )),
    path('brand/<int:pk>/', BrandView.as_view(
        {'get': 'list'}
    )),

]


urlpatterns = [
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
