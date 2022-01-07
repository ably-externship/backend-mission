from ..views import BaseView
from django.shortcuts import render
from missions.week_1.back.crud.sql.products.product import ProductCrud


def get_products(request):
    result = ProductCrud.get_products()
    return render(request, 'base.html', {'test': result})


class ProductBaseView(BaseView):
    pass


class ProductSearchView(ProductBaseView):
    pass