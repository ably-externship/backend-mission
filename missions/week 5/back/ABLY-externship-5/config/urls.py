"""config URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from accounts.urls import urlpatterns as accounts_urls
from products.urls import urlpatterns as products_urls
from products.customer_views import HomeView
from qna.urls import urlpatterns as qna_urls
from carts.urls import urlpatterns as carts_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(title='mbly', default_version='v1'),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    # swagger
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    
    # home
    path('', HomeView.as_view(), name='home'),
    
    # accounts
    path('accounts/', include(accounts_urls)),
    
    # products
    path('products/', include(products_urls)),
    
    # qna
    path('qna/', include(qna_urls)),
    
    # cart
    path('carts/', include(carts_urls)),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # debug toolbar
        path('__debug__/', include(debug_toolbar.urls)),
        # admin
        path('admin/', admin.site.urls),
]
