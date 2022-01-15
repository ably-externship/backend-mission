from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Product


def index(request):
    return render(request, 'product/product_list.html', make_response_data(1, ''))


def ajax(request):
    page_num = request.GET['page_num']
    q = request.GET['q']
    return JsonResponse(make_response_data(int(page_num), q), safe=False)


def detail(request, product_id):
    try:
        product = Product.objects.select_related('market_pk').get(id=product_id)
        product.file = product.files.all()
        context = {'product': product}
        return render(request, 'product/product_detail.html', context)
    except Product.DoesNotExist:
        return redirect('/404/')

def make_response_data(page_size, q):
    product_list = []
    #products = Product.objects.select_related('market_pk').select_related('category_fk').filter(Q(category__contains=q)|Q( name__contains=q))
    products = Product.objects.select_related('market_pk').select_related('category_fk').filter(Q(name__contains=q))
    paginator = Paginator(products, per_page=6)

    paging_product_list = paginator.page(page_size)
    for product in paging_product_list:
        file = product.files.first()
        product.file = file.file_path
        data = {
            'id': product.id,
            'company_name': product.market_pk.company_name,
            'file': file.file_path,
            'name': product.name,
            'price': product.price
        }
        product_list.append(data)

    response_data = {
        'num_pages': paginator.num_pages,
        'data' : product_list
    }
    return response_data

