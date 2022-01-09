from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = 'api'

urlpatterns = [
    path(r'v1/user/', include('api.user.urls', 'user')),
    path(r'v1/product/', include('api.product.urls', 'product')),
    path(r'v1/help/', include('api.help.urls', 'help')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)