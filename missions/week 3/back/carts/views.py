from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView

from carts.models import Cart
from products.models import ProductOption, Product


@login_required(login_url='users:login')
def cart_create(request, product_id):
    if request.method == 'POST':
        size = request.POST.get('size')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')

        product_option = ProductOption.objects.get(product_id=product_id, size=size, color=color)

        # 장바구니에 이미 있는 제품이면 업데이트하고 없으면 생성합니다.
        cart, _ = Cart.objects.get_or_create(user=request.user, product_id=product_id, product_option=product_option)
        cart.quantity = quantity
        cart.save()

        return redirect('carts:list')


class CartListView(ListView):
    model = Cart
    template_name = 'carts/cart_list.html'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'carts/cart_delete.html'
    success_url = reverse_lazy('carts:list')


@login_required(login_url='users:login')
def cart_update(request, pk, product_id):
    if request.method == 'POST':
        size = request.POST.get('size')
        color = request.POST.get('color')
        quantity = request.POST.get('quantity')

        product_option = ProductOption.objects.get(product_id=product_id, size=size, color=color)
        cart = Cart.objects.get(user=request.user, product_id=product_id, product_option=product_option)
        cart.size, cart.color, cart.quantity = size, color, quantity
        cart.save()
        return redirect(reverse('carts:list'))
    else:
        cart = Cart.objects.get(pk=pk)
        product = Product.objects.get(pk=product_id)
        return render(request, 'carts/cart_update.html', {'cart': cart, 'product': product})
