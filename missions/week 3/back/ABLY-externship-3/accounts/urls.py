from django.urls import include, path
from .customer_views import CustomerSignin, CustomerSignout, CustomerSignup, CustomerSocialLogin
from .seller_views import SellerSigninView, SellerSignupView, TokenRefreshView


app_name = 'accounts'

urlpatterns = [
    # customer
    path('signup', CustomerSignup.as_view(), name='signup'),
    path('login', CustomerSignin.as_view(), name='login'),
    path('login/social/kakao', CustomerSocialLogin.as_view(), name='kakao_login'),
    path('logout', CustomerSignout.as_view(), name='logout'),
    # seller
    path('sellers/signup', SellerSignupView.as_view(), name='seller_signup'),
    path('sellers/signin', SellerSigninView.as_view(), name='seller_signin'),
    path('sellers/tokenrefresh', TokenRefreshView.as_view(), name='token_refresh'),
]