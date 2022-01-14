"""mutbly URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import mutbly.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', mutbly.views.index, name='index'),
    path('items/<int:id>/', mutbly.views.show, name = 'show'),
    path('search/', mutbly.views.search, name='search'),
    path('items/<int:id>/questions/', mutbly.views.QuestionView.create, name='question_create'),
    path('items/<int:id>/questions/<int:cid>', mutbly.views.QuestionView.delete, name='question_delete'),
    path('accounts/signup/', accounts.views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/forgot_id/', accounts.views.forgot_id, name='find_id'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('search')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)