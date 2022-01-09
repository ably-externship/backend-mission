from django.urls import path
from . import views

urlpatterns = [
	path('', views.post, name='post'),
    path('redstore/', views.post_redstore, name='redstore'),
    path('redstore/redshirt/', views.post_redshirt, name='redshirt'),
    path('redstore/redskirt/', views.post_redskirt, name='redskirt'),
    path('redstore/reddress/', views.post_reddress, name='reddress'),
    path('redstore/board/', views.board, name='board'),
]