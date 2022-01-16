from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic

# Create your views here.
from carts.models import Cart
from products.models import ProductOption


@method_decorator(login_required, name='dispatch')
class CartView(generic.ListView):
    template_name = 'carts/cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


@login_required
def add_to_cart(request):
    user = request.user
    option = get_object_or_404(ProductOption, pk=request.POST['option'])
    quantity = request.POST['quantity']
    Cart(user=user, product_option=option, quantity=quantity).save()
    return redirect(reverse('cart'))


@login_required
def edit_cart(request, cart_id):
    user = request.user
    quantity = request.POST['quantity']
    cart = get_object_or_404(Cart, pk=cart_id, user=user)
    cart.quantity = quantity
    cart.save()
    return redirect(reverse('cart'))


@login_required
def remove_from_cart(request, cart_id):
    user = request.user
    cart = get_object_or_404(Cart, pk=cart_id, user=user)
    cart.delete()
    return redirect(reverse('cart'))
