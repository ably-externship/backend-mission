from hashlib import new
from math import prod
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *
from cart.models import Cart
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# from zoonbly.cart.models import Cart

# Create your views here.

def cart(request):
    user = request.user
    carts = Cart.objects.filter(user = user)
    paginator = Paginator(carts, 4)
    page = int(request.GET.get('page', 1))
    cart_list = paginator.get_page(page)
    return render(request, 'cart.html', {'cart_list': cart_list})

def addCart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    new_cart = Cart()
    new_cart.user = request.user
    new_cart.product = product
    new_cart.amount = request.POST['amount']
    product.cartNum = int(product.cartNum) + int(new_cart.amount)
    new_cart.save()
    product.save()
    return redirect('main:productDetail', product_id)

def deleteCart(request, cart_id):
    delete_cart = Cart.objects.get(pk = cart_id)
    product = delete_cart.product
    product.cartNum = int(product.cartNum) - int(delete_cart.amount)
    delete_cart.delete()
    product.save()
    return redirect('cart:cart')

def updateCart(request, cart_id):
    update_cart = Cart.objects.get(pk = cart_id)
    new_amount = request.POST['amount']
    product = update_cart.product
    product.cartNum = int(product.cartNum) - int(update_cart.amount) + int(new_amount)
    update_cart.amount = request.POST['amount']
    product.save()
    update_cart.save()
    return redirect('cart:cart')
