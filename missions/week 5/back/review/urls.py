from django.urls import path
from .views import *

app_name = 'review'

urlpatterns = [
    path('<int:product_id>', review_list, name='review_list'),
    path('register/<int:product_id>', review_create, name="review_create"),
    path('detail/<int:review_id>', review_detail, name="review_detail"),
    path('modify/<int:review_id>', review_modify, name="review_modify"),
    path('remove/<int:review_id>', review_delete, name="review_delete"),
    path('reviewbot', use_reviewbot, name="review_bot"),

]