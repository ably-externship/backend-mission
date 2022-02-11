from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('signup/', UserList.as_view(), name="signup"),
    path('current/', views.current_user),

    path('api/token/',MyTokenObtainPairView.as_view())
]