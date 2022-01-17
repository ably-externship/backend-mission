from statistics import quantiles
from django.shortcuts import render, redirect
from cart.models import InCartItem
from django.contrib.auth.models import User
from mutbly.models import Item



# Create your views here.


def show_cart(request):
  if request.user.is_authenticated:
    in_cart_items = InCartItem.objects.filter(user_id = request.user)
  return render(request, 'cart/cart.html', {'in_cart_items': in_cart_items})


def cart_num_count(request):
  in_cart_items = InCartItem.objects(user_id = request.user)
  in_cart_count = in_cart_items.len()
  print(in_cart_count)
  return render(request, 'mutbly/navbar.html', {"in_cart_count": in_cart_count})


def add_cart(request, id):
  if request.method=='POST' :
    item = Item.objects.get(id = id) 
    order_quantity = request.POST['order_quantity']
    in_cart_item = InCartItem()
    in_cart_item.user = request.user
    in_cart_item.item = item
    in_cart_item.quantity = order_quantity
    in_cart_item.save()    
    return redirect('index')
  else :
    return redirect('index')
    
  
def delete_cart(request, id) :
  delete_item = InCartItem.objects.get(id = id)
  delete_item.delete()
  return redirect('cart:show_cart')

def update_cart(request, id):
  if request.method=='POST' :
    update_item = InCartItem.objects.get(id = id)
    # print(request.POST.get('update_quantity'))
    update_item.quantity = request.POST['update_quantity']
    update_item.save()
    return redirect('cart:show_cart')
  else :
    return redirect('cart:show_cart')
    
  
  

  
    