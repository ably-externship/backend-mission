from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Seller
from shop.models import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductUploadForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        if Seller.objects.filter(user=request.user).exists():
            return HttpResponseRedirect('/')
        else:
            market_name = request.POST['market']
            make_market = Market.objects.create(name=market_name)
            market = get_object_or_404(Market, name=market_name)
            seller = Seller()
            seller.user = request.user
            seller.market = market
            seller.save()
            return render(request, 'seller/upload_product.html', {})
    return render(request, 'seller/register.html', {})



def upload_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        image = request.FILES["image"]
        product_upload = Product(
            name = name,
            category=category,
            image=image,
        )
        product_upload.save()
        return redirect('upload_product')
    else:
        productuploadForm = ProductUploadForm
        context = {
            'productuploadForm': productuploadForm,
        }
        return render(request, 'seller/upload_product.html', context)

