from cart.views import update
from django.urls import path
from django.urls.conf import include
from . import views
from .models import *
from accounts.views import token_on_header
# from rest_framework import routers


urlpatterns = [
    path('', views.page, name=''),
    path('RedStore/RedShirt/', views.post_RedShirt, name = 'RedShirt'),
    path('RedStore/RedDress/', views.post_RedDress, name = 'RedDress'),
    path('RedStore/', views.post_RedStore, name = 'RedStore'),
    path('RedStore/RedSkirt/', views.post_RedSkirt, name = 'RedSkirt'),
    path('redstore/items/', token_on_header, name='redstore_items'),
    path('items/add/',views.add_items, name='add_items'),
    path('items/update/<str:pk>/',views.update_items, name='update_items'),
    path('items/delete/<str:pk>/',views.delete_items, name='delete_items'),
    # path('redstore/', views.post_redstore, name='redstore'),
    # path('redstore/redshirt/', views.post_redshirt, name='redshirt'),
    # path('redstore/redskirt/', views.post_redskirt, name='redskirt'),
    # path('redstore/reddress/', views.post_reddress, name='reddress'),
    # path('api/',include('rest_framework.urls', namespace='rest_framework'))
]


# item_list = Item.objects.all()
# store_list=Store.objects.all()
# store_id=set()
# StoreAndItem=[]

# for item in item_list:
#     StoreAndItem.append((str(item.store_id_store)[-6:-1], item.name))
# StoreAndItem=list(set(StoreAndItem))



# url_lst=[]
# store_lst=[]
# for store_id, item in StoreAndItem:
#     for store in store_list:
#         store_lst.append(store.name)
#         if(store_id==store.id_store):
#             url_lst.append((store.name,item))
# url_lst=list(set(url_lst))
# store_lst=list(set(store_lst))
# url_lst.sort()


# # views_lst=[]
# # for method in dir(views):
# #     if 'post' in method:
# #         views_lst.append(method)
# # views_lst.sort()
# # print(views_lst)

# # # urlAndview = {}
# # # for url_item in url_lst:
# # #     urlAndview[url_item]=

# for store_name, item_name in url_lst:
#     item_url = path(store_name+'/'+item_name+'/', getattr(views, 'post_'+item_name), name=item_name)
#     urlpatterns.append(item_url)

# for store_name in store_lst:
#     # store_url=path(store_name+'/',getattr(views,'post_'+store_name),name=store_name)
#     store_url=path('RedStore/',getattr(views,'post_RedStore'),name='RedStore')

#     urlpatterns.append(store_url)

