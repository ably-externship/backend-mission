from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from cart.models import CartItem
from base.models import MallsItem



@login_required(login_url="/accounts/login")
def add_cart(request, id, num):
    # 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
    product = MallsItem.objects.get(id=id, num=num)
    user = request.user

    try:
        # 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
        cart = CartItem.objects.get(product__id=product.id, product__num=product.num, user=user)
        if cart:
            if cart.product.num == product.num:
                cart.quantity += 1
                cart.save()
            messages.warning(request, "장바구니에 상품이 담겼습니다.")
            return redirect(reverse('cart_page'))

    except CartItem.DoesNotExist:
        cart = CartItem(
            user = user,
            product=product,
            quantity=1,
        )
        cart.save()
        
    messages.warning(request, "장바구니에 상품이 담겼습니다.")
    return redirect('cart_page')


@login_required(login_url="/accounts/login")
def my_cart(request):
    """
    각 유저의 장바구니 공간
    """
    cart_item = CartItem.objects.filter(user__id=request.user.pk)
    if cart_item.exists():
        # 장바구니에 담긴 상품의 총 합계 가격
        total_price = 0
        # for loop 를 순회하여 각 상품 * 수량을 total_price 에 담는다
        for each_total in cart_item:
            total_price += each_total.product.sale_price * each_total.quantity
        if cart_item is not None:
            context = {
                # 없으면 없는대로 빈 conext 를 템플릿 변수에서 사용
                'cart_item': cart_item,
                'total_price': total_price,
            }
            return render(request, 'cart_list.html', context)

        return redirect('cart_page')

    else : 
        messages.warning(request, "장바구니가 비어있습니다.")
        return redirect('main_page')


@login_required(login_url="/accounts/login")
def delete_cart(request, id, num):
	# 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
    product = MallsItem.objects.get(id=id, num=num)
    user = request.user

    # 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
    cart = CartItem.objects.get(product__id=product.id, product__num=product.num, user=user)
    if cart:
        if cart.product.num == product.num:
            cart.delete()
        messages.warning(request, "장바구니에 상품이 삭제되었습니다.")
        return redirect(reverse('cart_page'))

    messages.warning(request, "오류가 발생하였습니다.")
    return redirect(reverse('cart_page'))


@login_required(login_url="/accounts/login")
def edit_cart(request, id, num):
    if request.method == "POST":
        # 상품을 담기 위해 해당 상품 객체를 product 변수에 할당
        product = MallsItem.objects.get(id=id, num=num)
        user = request.user
        edit_quantity = request.POST.get('edit_quantity')

        # 장바구니는 user 를 FK 로 참조하기 때문에 save() 를 하기 위해 user 가 누구인지도 알아야 함
        cart = CartItem.objects.get(product__id=product.id, product__num=product.num, user=user)
        if cart:
            if cart.product.num == product.num:
                cart.quantity = int(edit_quantity)
                cart.save()
            messages.warning(request, "장바구니에 상품이 수정되었습니다.")
            return redirect(reverse('cart_page'))

    else:
        messages.warning(request, "오류가 발생하였습니다.")
        return redirect(reverse('cart_page'))