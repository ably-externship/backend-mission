from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'products'
router = DefaultRouter()
router.register('', views.ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.ProductAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/options/', views.ProductOptionAPIView.as_view()),
    path('<int:pk>/options/<int:option_id>/', views.ProductOptionDetailAPIView.as_view()),

    # path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/question/", views.question, name="question"),
    path('search/', views.search, name='search'),
    path('me/', views.MyProductListView.as_view(), name='my-products'),
]
