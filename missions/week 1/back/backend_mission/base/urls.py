from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from base import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('accounts/', include('accounts.urls')),
    path('product/', include('product.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
