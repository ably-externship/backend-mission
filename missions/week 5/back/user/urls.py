from django.urls import path
from . import views
from .views import *

urlpatterns=[

    path('current/', views.current_user),
    path('api/token/',MyTokenObtainPairView.as_view()),

    # user_recommand관련
    path('recommand/', views.RecommandList, name="RecommandList"),
    path('recommand/create/', views.RecommandCreate, name="RecommandCreate"),
]