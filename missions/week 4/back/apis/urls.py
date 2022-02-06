from django.urls import path
from rest_framework import routers
from django.conf.urls import include 
from .views import MasterAdminViewSet, BrandAdminViewSet, RegisterBrandAPIView



router = routers.DefaultRouter()
#apis for items CRUD
router.register('master_admin', MasterAdminViewSet)
router.register('brand_admin', MasterAdminViewSet)

app_name = 'apis'

urlpatterns = [
    path('',include(router.urls)),
    path('accounts/',include('rest_auth.urls')),
    path('accounts/signup/',include('rest_auth.registration.urls')),
    path('brand/', RegisterBrandAPIView.as_view(), name= "register_brand"), 
]

