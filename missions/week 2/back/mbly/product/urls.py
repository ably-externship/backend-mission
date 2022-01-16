from django.urls import path,include
from .views import (ProductDetail, ProductList, SearchFormView,
question_create,question_detail,question_modify,question_delete,
answer_create,answer_detail,answer_modify,answer_delete,

)

"""
ENDPOINT : product/

"""
app_name = 'product'
urlpatterns = [
    path('list',ProductList.as_view(),name='list'),
    path('detail/<int:pk>',ProductDetail.as_view(),name='detail'),
    path('search',SearchFormView.as_view(),name='search'),

    path('question/<int:product_id>/add',question_create,name='question_add'),
    path('question/detail/<int:question_id>',question_detail,name='question_detail'),
    path('question/<int:question_id>/update',question_modify,name='question_update'),
    path('question/<int:question_id>/delete',question_delete,name='question_delete'),

    path('answer/<int:question_id>/add',answer_create,name='answer_create'),
    path('answer/detail/<int:answer_id>',answer_detail,name='answer_detail'),
    path('answer/<int:answer_id>/update',answer_modify,name='answer_update'),
    path('answer/<int:answer_id>/delete',answer_delete,name='answer_delete'),

    
]