from ..views import BaseView
from missions.week_1.back.crud.sql.products.product import ProductCrud
from django.shortcuts import redirect


class ProductBaseView(BaseView):
    pass


def get_products_view(request):
    products = ProductCrud.get_products(order_by='stars')
    data = {'products': products}
    return BaseView.response(request, 'page/product_list.html', data)


def search_products_view(request):
    keyword = request.POST.get('keyword')
    if len(keyword) < 1:
        return redirect('http://localhost:8000/api/v1/product/list')

    query = {
        'keyword': keyword,
        'where': 'name'
    }

    search_products = ProductCrud.search_products(query)
    data = {'products': search_products}
    return BaseView.response(request, 'page/product_list.html', data)


def product_detail(request, id):
    query = {
            'keyword': id,
            'where': 'id'
       }

    product = ProductCrud.search_products(query)
    data = {'product': product[0]}
    return BaseView.response(request, 'page/product_detail.html', data)
