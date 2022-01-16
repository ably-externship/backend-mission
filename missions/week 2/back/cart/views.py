from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from shop.models import Inventory, Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


# 장바구니 추가하기 ------
@login_required(login_url='login')
def add_cart(request):
    if request.method == 'POST':
        current_user = request.user
        selected_inventory = request.POST.get('inventory')
        selected_quantity = int(request.POST.get('quantity'))
        stock_now = Inventory.objects.get(id=selected_inventory).stock
        is_added = Cart.objects.filter(user_id=current_user, inventory_id=selected_inventory).exists()

        # 이미 추가된 상품이면 수량만 더하기 --
        if is_added:
            data = Cart.objects.get(user_id=current_user, inventory_id=selected_inventory)
            data.quantity += int(request.POST.get('quantity'))
            data.save()
            return redirect('/')

        # 품절 상품이면 추가 불가
        elif Inventory.objects.get(id=selected_inventory).stock == 0:
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        # 선택 수량이 재고보다 많다면 재고만큼만 추가
        elif selected_quantity > stock_now:
            cart = Cart()
            cart.user = current_user
            cart.inventory = Inventory.objects.get(id=selected_inventory)
            cart.quantity = stock_now
            cart.save()
            return redirect('/')

        else:
            cart = Cart()
            cart.user = current_user
            cart.inventory = Inventory.objects.get(id=selected_inventory)
            cart.quantity = selected_quantity
            cart.save()
            return redirect('/')


# 장바구니 페이지 ------
@login_required(login_url='login')
def cart_list(request):
    current_user = request.user
    user_cart = Cart.objects.filter(user_id=current_user)

    # 총 상품 가격 표시
    total_li = []
    for i in user_cart:
        price = i.inventory.product.price
        qty = i.quantity
        total_li.append(price*qty)
    total_price = sum(total_li)

    context = {'carts': user_cart,
                'total_price':total_price
               }
    return render(request, 'cart/list.html', context)



# 장바구니 상품 삭제 -----
@login_required(login_url='login')
def cart_delete(request, cart_id):
    selected_cart = get_object_or_404(Cart, pk=cart_id)
    selected_cart.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))



# 장바구니 상품 수량 수정 -----
@login_required(login_url='login')
def cart_modify(request, cart_id):
    if request.method == 'POST':
        selected_cart = get_object_or_404(Cart, pk=cart_id)
        modified_quantity = request.POST.get('quantity')
        stock_now = selected_cart.inventory.stock

        # 상품 수량 클릭 후 변경 없을 시
        if modified_quantity == "":
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        # 상품 변경 수량이 재고 보다 많을 시 재고 수량 적용
        elif int(modified_quantity) > stock_now:
            selected_cart.quantity = stock_now
            selected_cart.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

        # 상품 수량 변경
        else:
            selected_cart.quantity = modified_quantity
            selected_cart.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
