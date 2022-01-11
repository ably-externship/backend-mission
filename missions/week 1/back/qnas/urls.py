from django.urls import path

from qnas.question_views import QuestionView

urlpatterns = [
    path('/<int:product_id>', QuestionView.as_view()),
]