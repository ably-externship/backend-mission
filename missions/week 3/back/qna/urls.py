from django.urls import path
from . import views

urlpatterns = [
    path('qna/', views.qna_page, name="qna_page"),
    path('qna/<int:num>', views.qna_page_num, name="qna_page_num"),
]