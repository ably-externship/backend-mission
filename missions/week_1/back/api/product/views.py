from ..views import BaseView


class ProductBaseView(BaseView):
    pass


class ProductListView(ProductBaseView):
    _db = 'product'
    _table = 'product'
    pass


class ProductSearchView(ProductBaseView):
    pass