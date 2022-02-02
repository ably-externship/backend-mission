from django.urls import path
from . import views
from .views import MyTokenObtainPairView

urlpatterns=[

    path('current/', views.current_user),

    path('api/token/',MyTokenObtainPairView.as_view())
]