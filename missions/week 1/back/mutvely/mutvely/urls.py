"""mutvely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts
from markets import views as markets
from rest_framework import routers
from api.views import ProductViewSet

router = routers.DefaultRouter() 
router.register('product',ProductViewSet)

urlpatterns = [
    path('', markets.main, name='main'),
    path('admin/', admin.site.urls),

    path('login/', accounts.signin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', accounts.signup, name='signup'),
    path('mypage/', accounts.mypage, name='mypage'),
    path('cart/', accounts.cart, name='cart'),

    path('addCart/', markets.addcart, name='addcart'),
    path('CartCount/', markets.cartCount, name='cartCount'),
    path('removeCart/', markets.removeCart, name='removeCart'),

    path('outer/', markets.outer, name='outer'),
    path('top/', markets.top, name='top'),
    path('onepiece/', markets.onepiece, name='onepiece'),
    path('pants/', markets.pants, name='pants'),
    path('skirt/', markets.skirt, name='skirt'),

    path('<category>/search/', markets.search, name='searh'),
    path('<category>/product/<int:id>/', markets.detail, name='detail'),

    path('<category>/product/<int:id>/QnA/', markets.qna, name='qna'),
    
    url(r'^',include(router.urls)),
]
