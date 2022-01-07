from ..views import BaseView
from missions.week_1.back.crud.sql.products.product import ProductCrud
from missions.week_1.back.api.product.models import ProductQuery


def get_products_view(request):
    products = ProductCrud.get_products(order_by='stars')
    data = {
        'products': products
    }
    return BaseView.response(request, 'product_list.html', data)


def search_products_view(request):
    parameter = BaseView.get_parameter(request)

    product_query = ProductQuery()
    product_query.keyword = parameter.get('keyword')
    product_query.page = int(parameter.get('page')) if parameter.get('page') else 1
    product_query.display_cnt = int(parameter.get('display_cnt')) if parameter.get('display_cnt') else 10
    product_query.where = parameter.get('condition') or 'name'
    product_query.order_by = parameter.get('order_by') or 'stars'
    product_query.sort = parameter.get('sort_order') or 'DESC'

    search_products = ProductCrud.search_products(product_query)
    data = {
        'products': search_products
    }
    return BaseView.response(request, 'product_list.html', data)
