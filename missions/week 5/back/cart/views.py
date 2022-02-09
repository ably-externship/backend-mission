import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from product_option.models import ProductOption
from users.models import User


@login_required
@csrf_exempt
def cart_index(request):
    if request.method == 'POST':
        product_option_id = request.POST['product_option_id']
        quantity = request.POST['quantity']

        user_fk = request.session['user']
        user = User.objects.get(id=user_fk)

        product_option = ProductOption.objects.get(id=product_option_id)

        Cart.objects.create(product_option_fk=product_option, quantity=quantity, user_fk = user)

        response_data = {
            'result_code' : 'SUCCESS',
            'message': '장바구니에 상품이 담겼습니다',
            'data': 'None'
        }

        return JsonResponse(response_data, safe=False)
    else:
        user_fk = request.session['user']
        user = User.objects.get(id=user_fk)
        response_cart_list = []

        cart_list = Cart.objects.filter(user_fk=user)
        for cart in cart_list:
            file = cart.product_option_fk.product_pk.files.first()
            data = {
                'id': cart.id,
                'quantity': cart.quantity,
                'color': cart.product_option_fk.color,
                'size': cart.product_option_fk.size,
                'productName': cart.product_option_fk.product_pk.name,
                'file': file.file_path,
                'price': cart.product_option_fk.product_pk.price,
                'productId': cart.product_option_fk.product_pk.id
            }
            response_cart_list.append(data)
        context = {'cart_list': response_cart_list}
        return render(request, 'cart/cart_list.html', context)

@login_required
@csrf_exempt
def cart_delete_and_update(request, cart_id):
    #PUT Mapping 파라미터 받아올 수 있는 방법 확인 필요. request.PUT 동작 안함..
    if request.method == 'POST':
        cart = Cart.objects.get(id=cart_id)
        quantity = request.POST['quantity']
        cart.quantity = quantity
        cart.save()
        response_data = {
            'result_code' : 'SUCCESS',
            'message': '장바구니 상품의 수량이 변경되었습니다.',
            'data': 'None'
        }

        return JsonResponse(response_data, safe=False)
    elif request.method == 'DELETE':
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        response_data = {
            'result_code': 'SUCCESS',
            'message': '장바구니의 상품이 삭제되었습니다.',
            'data': 'None'
        }
        return JsonResponse(response_data, safe=False)


