from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.utils import timezone

# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-pub_date')
    return render(request, 'home.html', {'products':products})

def productNew(request):
    return render(request, 'productNew.html')

def productCreate(request):
    new_product = Product()
    new_product.name = request.POST['name']
    new_product.writer = request.user
    new_product.marcket = request.POST['marcket']
    new_product.pub_date = timezone.now()
    new_product.price = request.POST['price']
    new_product.stock = request.POST['stock']
    new_product.description = request.POST['description']
    new_product.image = request.FILES['image']
    new_product.save()
    return redirect('main:productDetail', new_product.id)

def productDetail(request, id):
    product = get_object_or_404(Product, pk = id)
    return render(request, 'productDetail.html', {'product':product})

def productEdit(request, id):
    edit_product = Product.objects.get(pk = id)
    return render(request, 'productEdit.html', {'product' : edit_product})

def productUpdate(request, id):
    update_product = Product.objects.get(pk = id)
    update_product.name = request.POST['name']
    update_product.writer = request.user
    update_product.marcket = request.POST['marcket']
    update_product.pub_date = timezone.now()
    update_product.price = request.POST['price']
    update_product.stock = request.POST['stock']
    update_product.description = request.POST['description']
    if request.FILES.get('image'):
        update_product.image = request.FILES.get('image')
    update_product.save()
    return redirect('main:productDetail', update_product.id)

def productDelete(request, id):
    delete_product = Product.objects.get(pk = id)
    delete_product.delete()
    return redirect('main:home')