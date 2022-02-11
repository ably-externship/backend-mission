"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from base.views import CustomHandler500, CustomHandler404
from product.urls import urlpatterns as product_url
from users.urls import urlpatterns as auth_url
from board.urls import urlpatterns as board_url
from cart.urls import urlpatterns as cart_url
from product.api.urls import urlpatterns as products_url
from users.api.urls import urlpatterns as auth_token_url
from market.api.urls import urlpatterns as market_url
from product_category.api.urls import urlpatterns as product_category_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(product_url)),
    path('auth/', include(auth_url)),
    path('auth/', include(auth_token_url)),
    path('board/', include(board_url)),
    path('404/', CustomHandler404.as_view()),
    path('500/', CustomHandler500.as_view()),
    path('cart/', include(cart_url)),
    path('products/', include(products_url)),
    path('markets/', include(market_url)),
    path('product-categorys/', include(product_category_url))
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
