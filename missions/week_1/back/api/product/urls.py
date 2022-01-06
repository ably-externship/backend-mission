from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.ProductListView.as_view()),
    path('search/', views.ProductSearchView.as_view()),
    path('detail/', include('detail.urls'))
]