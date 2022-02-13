from django.urls import path
from . import views

urlpatterns = [
    # path('',views.board_list, name='board'),
    # path('write/',views.board_write, name='board_write')
    path('', views.board, name='board'),
    path('edit/<int:pk>', views.boardEdit, name='edit'),
    path('delete/<int:pk>', views.boardDelete, name='delete'),
]
