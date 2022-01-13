from django.urls import path
from .views import UserLoginView, UserCreateView, UserLogoutView, CommentCreateView, CartAddView

urlpatterns = [
    # user api
    path('v1/user/login/', UserLoginView.as_view(), name='apis_v1_user_login'),
    path('v1/user/logout/', UserLogoutView.as_view(), name='apis_v1_user_logout'),
    path('v1/user/create/', UserCreateView.as_view(), name='apis_v1_user_create'),

    # cart api
    path('v1/cart/add/', UserCreateView.as_view(), name='apis_v1_cart_add'),

    # comment api
    path('v1/comment/create/', CommentCreateView.as_view(), name='apis_v1_comment_create'),
]
