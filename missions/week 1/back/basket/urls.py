from django.urls import path
from .views import basket_create, basket_list,basket_update,basket_delete_v2

urlpatterns = [
    path('<int:item>', basket_create, name="basket_create"),
    path('mypage', basket_list, name="mypage"),
    path('basket/item/v2/<int:user>', basket_delete_v2, name="deletev2"),

    path('item/<int:user>', basket_update, name="updatev2"),

]