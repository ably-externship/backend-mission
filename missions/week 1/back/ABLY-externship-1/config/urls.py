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
from django.views.generic import TemplateView
from accounts.views import UserSignup, UserLogin
from products.views import MerchandiseALL, MerchandiseDetail, QuestionNew

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # accounts
    path('', MerchandiseALL.as_view(), name='home'),
    path('accounts/signup', UserSignup.as_view(), name='signup'),
    path('accounts/login', UserLogin.as_view(), name='login'),
    # products
    path('products/detail/<int:pk>', MerchandiseDetail.as_view(), name='product_detail'),
    # questions
    path('questions/new/', QuestionNew.as_view(), name='question_new'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        # debug toolbar
        path('__debug__/', include(debug_toolbar.urls)),
]