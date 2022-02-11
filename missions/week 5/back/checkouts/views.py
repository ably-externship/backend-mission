from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import ListView

# Create your views here.
from iamport import Iamport

from accounts.forms import AddressForm
from base.settings.common import IAMPORT_REST_API_KEY, IAMPORT_REST_API_SECRET
from carts.models import Cart
from .forms import *


@login_required
@require_GET
def checkout(request: HttpRequest) -> HttpResponse:
    items = Cart.objects.filter(user=request.user)
    if len(items) == 0:
        return redirect(reverse('cart'))
    return render(request, 'checkouts/checkout.html', {
        'items': items,
        'quantity': len(items),
        'total': sum(map(lambda e: e.get_price(), items)),
        'buyer_form': BuyerForm(initial={
            'buyer_name': request.user.name,
            'buyer_email': request.user.email
        }),
        'address_form': AddressForm(initial={
            'name': request.user.name
        }),
        'payment_method_form': PaymentMethodForm()
    })


@login_required
@require_POST
def submit(request: HttpRequest) -> HttpResponse:
    items = Cart.objects.filter(user=request.user)
    if len(items) == 0:
        return HttpResponseNotFound("장바구니가 비어 있음")
    payment_method = get_object_or_404(PaymentMethod, pk=request.POST['payment_method'])
    name = items[0].product_option.product.display_name
    if len(name) > 8:
        name = name[:8]
    if len(items) > 1:
        name += f' 외 {len(items) - 1}'
    amount = sum(map(lambda e: e.get_price(), items))
    address = Address(user=request.user, name=request.POST['name'], address=request.POST['address'],
                      postal_code=request.POST['postal_code'], extra_address=['extra_address'],
                      phone=request.POST['phone'])
    address.save()
    transaction = Transaction.create_transaction(user=request.user, method=payment_method, name=name, amount=amount,
                                                 address=address)
    for item in items:
        TransactionItem(transaction=transaction, product_option=item.product_option, quantity=item.quantity,
                        unit_price=item.product_option.get_price()).save()
    return render(request, 'checkouts/submit.html', {
        'pg': payment_method.pg,
        'pay_method': payment_method.pay_method,
        'order_id': transaction.order_id,
        'name': transaction.name,
        'amount': transaction.amount,
        'buyer_name': request.POST['buyer_name'],
        'buyer_email': request.POST['buyer_email'],
        'buyer_tel': request.POST['buyer_tel']
    })


@login_required
@require_GET
def verify(request: HttpRequest) -> HttpResponse:
    def verify_by_iamport(imp_uid: str, merchant_uid: str, amount: int) -> bool:
        iamport = Iamport(imp_key=IAMPORT_REST_API_KEY, imp_secret=IAMPORT_REST_API_SECRET)
        try:
            response = iamport.find(imp_uid=imp_uid, merchant_uid=merchant_uid)
            return iamport.is_paid(amount, response=response)
        except (Iamport.ResponseError, Iamport.HttpError):
            return False

    receipt_id = str(request.GET['receipt_id'])
    order_id = str(request.GET['order_id'])
    transaction = get_object_or_404(Transaction, order_id=order_id)
    if transaction.status == 'ready' and verify_by_iamport(receipt_id, order_id, transaction.amount):
        transaction.receipt_id = receipt_id
        transaction.status = 'paid'
        transaction.save()
        request.session['order_id'] = order_id
        return redirect(reverse('succeeded'))
    else:
        return HttpResponseForbidden('결제 검증 실패')


@login_required
@require_GET
def succeeded(request: HttpRequest) -> HttpResponse:
    if 'order_id' not in request.session.keys():
        return redirect(reverse('index'))
    order_id = request.session['order_id']
    del request.session['order_id']
    Cart.objects.filter(user=request.user).delete()
    transaction = get_object_or_404(Transaction, order_id=order_id)
    items = TransactionItem.objects.filter(transaction=transaction)
    return render(request, 'checkouts/succeeded.html', {
        'order_id': order_id,
        'transaction': transaction,
        'items': items
    })


class TransactionListView(ListView):
    template_name = 'checkouts/list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-created_at')
