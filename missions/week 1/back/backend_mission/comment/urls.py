from django.urls import path

from comment.views import CommentCreateView

app_name = 'comment'

urlpatterns = [
    path('create/', CommentCreateView.as_view(), name='create'),

]