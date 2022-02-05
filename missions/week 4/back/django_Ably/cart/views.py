from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from markets.models import Item
from accounts.models import AuthUser
from .models import Cart
from collections import defaultdict


def add_cart(request):
    # users=AuthUser.objects.all()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        
    else:
        return redirect('')
    login_user = AuthUser.objects.get(username=username)
    login_user_id = login_user.id
    select_color = request.POST.get('color')
    select_size = request.POST.get('size')
    select_item = request.POST.get('item')
    select_quantity = request.POST.get('quantity')
    item=Item.objects.filter(color=select_color, size=select_size, name = select_item)
    item_id=item[0].id_item

    cart_instance = Cart.objects.create(
        auth_user_id=login_user_id,
        item_id_item=item[0],
        quantity=select_quantity)
    
    # usercart=Cart.objects.filter(arth_user=username)
    return redirect('/cart')

def view_cart(request):
    if request.user.is_authenticated:
        username = request.user.username
    login_user = AuthUser.objects.get(username=username)
    cart_items = Cart.objects.filter(auth_user=login_user)
    user_cart = []
    for cart_item in cart_items:
        item_info = Item.objects.get(id_item=cart_item.item_id_item.id_item)
        user_cart.append([cart_item.id,item_info.name,item_info.size, item_info.color, cart_item.quantity, item_info.price*cart_item.quantity] )
    context = {'cart_items':user_cart}
    return render(request, 'cart.html',context )


def update(request,pk):
    
    select_quantity = request.POST.get('quantity')
    print(select_quantity,pk)

    if request.user.is_authenticated:
        username = request.user.username
    login_user = AuthUser.objects.get(username=username)
    cart_items = Cart.objects.get(auth_user=login_user, id = pk)
    cart_items.quantity = select_quantity
    cart_items.save()
    return redirect('/cart')


def delete(request,pk):

    select_quantity = request.POST.get('quantity')
    print(select_quantity,pk)

    if request.user.is_authenticated:
        username = request.user.username
    login_user = AuthUser.objects.get(username=username)
    cart_items = Cart.objects.get(auth_user=login_user, id = pk)
    
    cart_items.delete()
    return redirect('/cart')


