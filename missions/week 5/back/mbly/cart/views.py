from math import prod
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Cart,Order
from django.contrib import messages
from product.models import RealProduct,Product
# Create your views here.




def cart_list(request):
    """
    장바구니 리스트
    """
    queryset = Cart.objects.filter(user = request.user)
    context = {}
    context["object_list"]= queryset
    total = 0
    for cart in queryset: # 전체금액 계산
        total+=cart.total_price()
    context['total']=total
    return render(request,"cart/cart_list.html",context)


def cart_add(request):
    """
    장바구니 추가
    """
    print(request.GET)
    realproduct_id = request.GET['id']
    print(realproduct_id)
    object = get_object_or_404(RealProduct,pk = realproduct_id)
    if Cart.objects.filter(user = request.user, product = object): # 이미 존재
        cart = Cart.objects.get(user=request.user,product=object)
        cart.quantity +=1
        cart.save()
    else:
        Cart.objects.create(
            user = request.user,
            product = object,
            quantity = 1
            
        )
    return redirect('cart:list')

def cart_update(request):
    """
    장바구니 수량 변경
    """
    cart_id = request.GET['id']
    cart = get_object_or_404(Cart,pk=cart_id)
    number = int(request.GET['number'])
    if number <=0 :
        messages.error(request,"상품 수량을 다시 확인해주세요")
        return redirect('cart:list')

    productReal = cart.product
    if number > productReal.stock_quantity : # 현재 실제 상품의 재고확인
        messages.error(request,"남은 재고를 확인해주세요")
        print("fail")
        return redirect('cart:list')
    else:
        cart.quantity = number
        messages.success(request,cart.product.product.name+" 수량 Update ")
        cart.save()
        return redirect('cart:list')

def cart_delete(request):
    """
    장바구니 제거
    """
    cart_id = request.GET['id']
    cart = get_object_or_404(Cart,pk = cart_id)
    if cart.user == request.user: # 유저 같은지 판단
        cart.delete()
        messages.success(request," 삭제 성공")
        
        return redirect('cart:list')
    messages.error(request,"유저가 다릅니다")
    return redirect('cart:list')


def product_purchase(request):
    """
    상품 구매
    """
    selected = request.GET.getlist('selected')
    for id in selected:
        cart = Cart.objects.select_related('product__product').select_related('product__product__market').get(pk=id)
        realproduct = cart.product
        product = realproduct.product
        market = product.market

        # 구매이력
        Order.objects.create(
            user = request.user,
            market = market,
            realproduct = realproduct,
            product = product,
            product_num = cart.quantity,
            per_price = realproduct.add_price+product.sale_price,
            total_price = cart.quantity*(realproduct.add_price+product.sale_price),
        )

        cart.delete() # 카트 삭제
    messages.success(request," 구매 성공")
    return redirect('product:list')
    