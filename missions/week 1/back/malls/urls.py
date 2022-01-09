from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('main/', views.main, name='main_page'),
    path('login/', views.login, name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('shops/<int:id>', views.shops, name="shop"),
    path('shops/<int:id>/<int:num>', views.item_page, name="item_page"),
    path('search/', views.search_page, name="search_page"),
    path('questionboard/', views.board_page, name="board_page"),
    path('questionboard/<int:num>', views.board_page_num, name="board_page_num"),
]