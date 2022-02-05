from django.urls import path
import cart.views

app_name = 'cart'

urlpatterns = [
    path('', cart.views.show_cart, name='show_cart'),
    path('<int:id>/add_cart/', cart.views.add_cart, name='add_cart'),
    path('<int:id>/delete_cart/', cart.views.delete_cart, name='delete_cart'),
    path('<int:id>/update_cart/', cart.views.update_cart, name='update_cart'),
    
    
]

