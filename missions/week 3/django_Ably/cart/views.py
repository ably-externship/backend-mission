from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from markets.models import Item
from accounts.models import AuthUser
from .models import Cart
from collections import defaultdict
# Create your views here.

# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# def add_cart(request, item_id):
#     item = Item.objects.get(id_item=item_id)
#     try:
#         cart = Cart.objects.get(id_cart = _cart_id(request))
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             id_cart = _cart_id(request)
#         )
#         cart.save()
    
#     try:
#         cart_item = Cartitem.objects.get(item_id_item=item,cart_id_cart=cart)
#         cart_item.quantity +=1
#         cart_item.save()
#     except Cartitem.DoesNotExist:
#         cart_item = Cartitem.objects.create(
#             item_id_item = item,
#             quantity=1,
#             cart_id_cart=cart
#         )
#         cart_item.save()
#     return redirect('cart:cart_detail')

# def cart_detail(request, total=0, counter=0, cart_items = None):
#     try:
#         cart = Cart.objects.get(id_cart=_cart_id(request))
#         cart_items = Cartitem.objects.filter(cart_id_cart=cart)
#         for cart_item in cart_items:
#             total += (cart_item.item_id_item.price * cart_item.quantity)
#             counter += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass

#     return render(request, 'cart.html', dict(cart_items = cart_items, total=total, counter = counter))


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


