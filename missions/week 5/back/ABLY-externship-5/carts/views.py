from ast import Delete
from gc import get_objects
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import RedirectView
from products.models import BaseMerchandise, Merchandise
from .forms import AddMerchandiseForm
from .cart import Cart

# Create your views here.


class CartAddView(RedirectView):
    
    def post(self, request, pk, *args, **kwargs):
        merchandise = get_object_or_404(Merchandise, id=pk)
        form = AddMerchandiseForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            is_updated = form.cleaned_data['is_updated']
            Cart(request).add(
                merchandise=merchandise,
                quantity=quantity,
                is_updated=is_updated
            )
        return redirect(f'http://127.0.0.1:8000/products/detail/{merchandise.basemerchandise}')


class CartUpdateView(View):
    
    def post(self, request, pk, *args, **kwargs):
        form = AddMerchandiseForm(request.POST)
        quantity = str(form['quantity'].value())
        merchandise = get_object_or_404(Merchandise, id=pk)
        Cart(request).update(str(merchandise), quantity)
        
        return redirect('cart_detail')


class CartDeleteView(View):
    
    def post(self, request, pk, *args, **kwargs):
        
        merchandise = get_object_or_404(Merchandise, id=pk)
        Cart(request).delete(str(merchandise))
        
        return redirect('cart_detail')


class CartClearView(View):
    
    def post(self, request, *args, **kwargs):
        
        Cart(request).clear()
        context = {
            'cart': Cart(request)
        }
        return render(request, 'carts/cart.html', context)


class CartDetailView(View):
    
    def get(self, request, *args, **kwargs):
        
        for merchandise in Cart(request):
            merchandise['quantity_form'] = AddMerchandiseForm(
                initial={
                    'quantity': merchandise['quantity'],
                    'is_updated': True
                }
            )
        context = {
            'cart': Cart(request),
            'form': AddMerchandiseForm()
        }
        return render(request, 'carts/cart.html', context)