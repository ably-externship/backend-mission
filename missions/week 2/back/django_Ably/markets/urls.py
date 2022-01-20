from django.urls import path
from . import views
from .models import *
urlpatterns = [
    path('', views.page, name=''),
    # path('redstore/', views.post_redstore, name='redstore'),
    # path('redstore/redshirt/', views.post_redshirt, name='redshirt'),
    # path('redstore/redskirt/', views.post_redskirt, name='redskirt'),
    # path('redstore/reddress/', views.post_reddress, name='reddress'),
]

store_list = Store.objects.all()
for store in store_list:
    url = path(store.name, getattr(views, 'post_redstore'), name=store.name)
    urlpatterns.append(url)