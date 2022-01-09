from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Product

def product_list(request):
    page = request.GET.get('page', '1')
    products = Product.objects.all()
    paginator = Paginator(products, '2')
    page_products = paginator.get_page(page)

    return render(request, 'mall/product_list.html', {'page_products': page_products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'mall/product_detail.html', {'product': product})
