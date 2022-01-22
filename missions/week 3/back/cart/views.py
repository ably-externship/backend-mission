from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Cart
from .models import CartItem
from .models import User
from .models import Product

from project.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def cart(request):

    if request.method == "GET":
        user = User.objects.get(email=request.user)
        cart = Cart.objects.get(user=user)

        # 파이썬에서 데이터 가공 -> DB에서로 수정 필요
        cart_item = CartItem.objects.filter(cart=cart)
        products = Product.objects.all()

        selected_products = []
        for item in cart_item:
            for product in products:
                if item.product.id == product.id:
                    if product.id not in selected_products:
                        selected_products.append(product)
        #

    ctx = {
        'products': selected_products,
        'cart_items': cart_item
    }

    return render(request, 'cart/index.html', ctx)


@login_required(login_url=LOGIN_URL)
def add_cart(request, product_id):
    if request.method == 'POST':
        user = User.objects.get(email=request.user)
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            CartItem.objects.filter(cart=cart, product=product).update(
                quantity=cart_item.quantity + 1)
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=1)

    return redirect('cart:cart')


def plus_cart(request, product_id):
    if request.method == 'POST':
        user = User.objects.get(email=request.user)
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        CartItem.objects.filter(cart=cart, product=product).update(
            quantity=cart_item.quantity + 1)

    return redirect('cart:cart')


def minus_cart(request, product_id):
    if request.method == 'POST':
        user = User.objects.get(email=request.user)
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            CartItem.objects.filter(cart=cart, product=product).update(
                quantity=cart_item.quantity - 1)
        else:
            messages.warning(request, "최소 1개 이상 구매 가능합니다.")

    return redirect('cart:cart')


def delete_cart(request, product_id):
    if request.method == 'POST':
        user = User.objects.get(email=request.user)
        product = Product.objects.get(pk=product_id)
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()

    return redirect('cart:cart')
