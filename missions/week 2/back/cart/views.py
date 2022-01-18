from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from product.models import Product, Product_options
from user.models import Account

from .forms import AddProductForm
from .cart import Cart

@require_POST
def add(request):
    cart = Cart(request)
    select_option_id = request.POST.get('opt')
    size = Product_options.objects.get(id=select_option_id).opt1_name
    add_price = Product_options.objects.get(id=select_option_id).opt1_price
    product = Product_options.objects.get(id=select_option_id).product

    form = AddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'], opt_size=size, opt_price=add_price)

    return redirect('cart:detail')

def remove(request, cart_id):
    cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    cart.remove(cart_id)
    return redirect('cart:detail')

def detail(request):
    # 카카오톡 토큰
    context={}
    if request.session.get('access_token'):
        context['check'] = True
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
    context['carts']=cart


    return render(request, 'cart.html', context)