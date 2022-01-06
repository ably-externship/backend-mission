from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='product/list.html'), name='list')
]