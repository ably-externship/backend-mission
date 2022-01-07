from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Product


def index(request):
    return render(request, 'product/product_list.html', make_response_data(1))


def ajax(request):
    page_num = request.GET['page_num']
    return JsonResponse(make_response_data(int(page_num)), safe=False)


def detail(request, product_id):
    product = Product.objects.select_related('market_pk').get(id=product_id)
    product.file = product.files.all()
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def make_response_data(page_size):
    product_list = []
    products = Product.objects.select_related('market_pk').all()
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

