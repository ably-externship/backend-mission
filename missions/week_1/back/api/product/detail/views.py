from ..views import BaseView
from missions.week_1.back.crud.sql.products.product import ProductCrud


def get_product_view(request):
    product_id = request.get('id')
    data = {}
    return BaseView.response(request, 'product_detail.html', data)