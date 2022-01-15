from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

import account

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('account.urls')),
  path('oauth/', account.views.oauth, name='oauth'),
  path('', TemplateView.as_view(template_name='base.html'), name='base'),
  path('product/', include('product.urls')),
  path('comment/', include('comment.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
