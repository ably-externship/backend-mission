from hashlib import new
from math import prod
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from main.models import *
from cart.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# from zoonbly.cart.models import Cart

# Create your views here.

# 장바구니 페이지 / 상품 총 금액 및 할인 이벤트 적용
def cart(request):
    user = request.user
    carts = Cart.objects.filter(user = user)
    total = 0
    final = 0
    finalPrice = 0
    categoNum = 0
    catego = []
    for cart in carts:
        total = total + cart.optionPrice
    for cart in carts:
        if cart.product.category not in catego:
            catego.append(cart.product.category)
            categoNum = categoNum + 1
    if categoNum > 1:
        final = total - total*(categoNum*2+1)/100
        finalPrice = round(final)
    else:
        finalPrice = total
    paginator = Paginator(carts, 4)
    page = int(request.GET.get('page', 1))
    cart_list = paginator.get_page(page)
    return render(request, 'cart.html', {'cart_list': cart_list, 'total':total, 'catego':catego, 'categoNum':categoNum, 'final':finalPrice})

# 상품 추가 수정 삭제
def addCart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    new_cart = Cart()
    new_cart.user = request.user
    new_cart.product = product
    selectedOption = request.POST.get('option')
    new_cart.option = get_object_or_404(Options, pk = selectedOption)
    new_cart.amount = request.POST['amount']
    new_cart.optionPrice = int(new_cart.option.price) * int(new_cart.amount)
    new_cart.save()
    return redirect('main:productDetail', product_id)

def deleteCart(request, cart_id):
    delete_cart = Cart.objects.get(pk = cart_id)
    product = delete_cart.product
    delete_cart.delete()
    return redirect('cart:cart')

def updateCart(request, cart_id):
    update_cart = Cart.objects.get(pk = cart_id)
    new_amount = request.POST['amount']
    product = update_cart.product
    update_cart.amount = request.POST['amount']
    update_cart.optionPrice = int(update_cart.option.price) * int(update_cart.amount)
    update_cart.save()
    return redirect('cart:cart')

# 상품 구매 후 구매 목록 페이지
def purchasePage(request):
    user = request.user
    purchases = Purchase.objects.filter(user = user).order_by('-pur_date')
    return render(request, 'purchase.html', {'purchases':purchases})

def purchase(request):
    user = request.user
    carts = Cart.objects.filter(user = user)
    for cart in carts:
        new_purchase = Purchase()
        new_purchase.user = request.user
        new_purchase.product = cart.product
        new_purchase.option = cart.option
        new_purchase.amount = cart.amount
        new_purchase.totalPrice = cart.optionPrice
        new_purchase.status = '배송중'
        new_purchase.save()
        cart.delete()
    purchases = Purchase.objects.filter(user = user).order_by('-pur_date')
    return render(request, 'purchase.html', {'purchases':purchases})