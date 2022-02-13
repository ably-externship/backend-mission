from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
import requests

from .models import Product, Category, Brand, Image, Comment, Cart


# 카카오페이 결제
class KaKaoPayView(TemplateView):
    template_name = 'pay/kakaoPay.html'

    def get_context_data(self, **kwargs):
        context = super(KaKaoPayView, self).get_context_data(**kwargs)

        user_id = self.request.user.id
        cart = Cart.objects.filter(user_id=user_id)
        total_price = 0

        for cart in cart:
            total_price += cart.product.price * cart.quantity

        if cart is not None:
            context['total'] = total_price
            total = total_price

        cart_product = Cart.objects.filter(user_id=user_id).all()
        product_ids = list(cart_product.values_list('product_id', flat=True))
        carts = Cart.objects.select_related('product').filter(user__in=[self.request.user])

        product_list = []
        if carts.exists:
            for cart in carts:
                if cart.product.id in product_ids:
                    product_list.append(cart.product.name)

        context['products'] = product_list[0]
        context['product_count'] = len(product_list) - 1

        return context


# 카카오페이 로직
def KaKaoPayLogic(request):
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id)
    total_price = 0

    for cart in cart:
        total_price += cart.product.price * cart.quantity

    if cart is not None:
        total = total_price

    cart_product = Cart.objects.filter(user_id=user_id).all()
    product_ids = list(cart_product.values_list('product_id', flat=True))
    carts = Cart.objects.select_related('product').filter(user__in=[request.user])

    product_list = []
    if carts.exists:
        for cart in carts:
            if cart.product.id in product_ids:
                product_list.append(cart.product.name)

        # admin key
        admin_key = 'f2208204a0ec99434a5f2176633d8096'
        # pay api
        _url = f'https://kapi.kakao.com/v1/payment/ready'
        # header data
        _headers = {
            'Authorization': f'KakaoAK {admin_key}',
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }

        _data = {
            'cid': 'TC0ONETIME',
            'partner_order_id': 'partner_order_id',
            'partner_user_id': f'{user_id}',
            'item_name': '{} 외 {}개'.format(product_list[0], len(product_list) - 1),
            'quantity': f'{len(product_list)}',
            'total_amount': f'{total}',
            'tax_free_amount': '0',
            'approval_url': 'http://127.0.0.1:8000/paySuccess/',
            'fail_url': 'http://127.0.0.1:8000/payFail/',
            'cancel_url': 'http://127.0.0.1:8000/payCancel/',
        }

        res = requests.post(_url, data=_data, headers=_headers)
        if res.status_code == 200:
            print("성공")
        else:
            print("실패")
        request.session['tid'] = res.json()['tid']
        return redirect(res.json()['next_redirect_pc_url'])


# 카카오페이 성공
def PaySuccess(request):
    url = 'https://kapi.kakao.com/v1/payment/approve'
    admin_key = 'f2208204a0ec99434a5f2176633d8096'
    headers = {
        'Authorization': f'KakaoAK {admin_key}',
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    res = requests.post(url, data=data, headers=headers)
    result = res.json()
    if result.get('msg'):
        return redirect('/pay/payFail/')
    else:
        # * 사용하는 프레임워크별 코드를 수정하여 배포하는 방법도 있지만
        #   Req Header를 통해 분기하는 것을 추천
        # - Django 등 적용 시
        return render(request, 'pay/paySuccess.html')
        # # - React 적용 시
        # return redirect('http://localhost:3000')


def payFail(request):
    return render(request, 'pay/payFail.html')


def payCancel(request):
    return render(request, 'pay/payCancel.html')

